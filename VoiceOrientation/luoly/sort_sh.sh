#!/bin/sh

#有一个参数，为要处理的文件
# usage:
#	Firstly, change the current directory to the directory of file which need to handle
# 	then exectue the command "./sort_sh.sh filename"



curdir=$(pwd)
cd $curdir
filename=$1

num=$(cat "$filename" | wc -l)
row1=1
row2=3

while [ "$row2" -le "$num" ]
do
	sed -n "${row1},${row2}p" $filename | sort >> temp
	row1=$((row1+3))
	row2=$((row2+3))
done

cat temp | cut -d ' ' -f 3,4,5,6 | cut -d ']' -f 1 > result
rm temp

exit 0
