# formatting data
import sys

origin_file = sys.argv[1]
change_file = sys.argv[2]

file = open(origin_file)
datas = file.readlines()
file_new = open(change_file, 'w')
count = 1
for i in range(len(datas)):
    datas[i] = datas[i].replace('[', '')
    datas[i] = datas[i].replace(']', '')
    data = datas[i].strip('\n').split(', ')

    file_new.write('1 ')
    # file_new.write('-1 ')
    count = 1
    for j in range(len(data)):
        file_new.write(str(count))
        file_new.write(':')
        file_new.write(str(data[j]))
        count += 1
        file_new.write(' ')
    file_new.write('\n')
file.close()
file_new.close()
