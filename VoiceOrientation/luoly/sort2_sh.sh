#!/bin/bash

# usage:
# 	有三个参数，前两个参数为要排序的文件名，第三个参数表明第一个参数是人声还是机器的回放声
#	./sort2_sh.sh filename1 filename2 voicecomefrome


curdir=$(pwd)
cd $curdir
filename1="$1"
filename2="$2"
name1=""
name2=""


num=$(cat "$filename1" | wc -l)
row1=1
row2=3

if [ "$3" = "h" ]; then
	name1=human
	name2=machine
elif [ "$3" = "m" ]; then
	name1=machine
	name2=human
fi

while [ "$row2" -le "$num" ]
do
	sed -n "${row1},${row2}p" $filename1 | sort >> temp1
	sed -n "${row1},${row2}p" $filename2 | sort >> temp2
	row1=$((row1+3))
	row2=$((row2+3))
done

cat temp1 | cut -d ' ' -f 3,4,5,6 | cut -d ']' -f 1 > log_${name1}.${name1}
cat temp2 | cut -d ' ' -f 3,4,5,6 | cut -d ']' -f 1 > log_${name2}.${name2}
rm temp1 temp2

exit 0
