#!/bin/bash

# Current directory is luoly
# 该脚本需要一个参数，含义是声音来自人声还是机器回放
# luoly目录下需要有 log_human log_machine 文件，因为 mathanalysis.py 同时需要
# log_human.human log_machine.machine, 所以需要同时为 log_human log_machine排序，但是实时测试时候
# 只能实时产生一组数据（人或者机器），所以luoly目录下要放置提前录好的 log_human log_machine 来补上实时
# 测试的时候空缺的数据


vcomef="$1"						#机器或者人声
anvcomef=""


if [ "$#" != 1 ]; then
	echo "Please input source of the voice: "m" or "h" "
	exit 1
fi


cd sound 
rm -rf log
mkdir log
python kws_cch.py
cd ..
rm log
python generatePar.py sound/log/test
python generateResult.py sound/log/test


# classify


if [ "$vcomef" = "h" ]; then
	anvcomef="machine"
elif [ "$vcomef" = "m" ]; then 
	anvcomef="human"
fi

sh sort2_sh.sh log log_${anvcomef} $vcomef

cp log_human.human log_machine.machine ../libsvm/python
cd ../libsvm/python
python mathanalysis.py log_human.human log_machine.machine newlog_h newlog_m
python format.py newlog_${vcomef} newlog_${vcomef}_formated
python classifyData.py newlog_${vcomef}_formated


exit 0
