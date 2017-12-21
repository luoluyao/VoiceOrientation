import sys


def main():

    # groundtruth data file
    standardFile = sys.argv[1]
    # test data file
    testFile = sys.argv[2]
    # new data file
    newDataFile = sys.argv[3]
    new_data_file = open(newDataFile, 'w')

    stand_file = open(standardFile)
    stand_data = stand_file.readlines()
    # groundtruth data array
    stand_datas = []
    for s_data in stand_data:
        d = s_data.split(" ")
        stand_datas.append(d)

    test_file = open(testFile)
    test_data = test_file.readlines()
    line_count = 0
    for t_data in test_data:
        t_data = t_data.replace('[', '')
        t_data = t_data.replace(']', '')
        t_ds = t_data.split(", ")
        row_count = 0
        for t_d in t_ds:
            v = float(stand_datas[line_count % 3][row_count]) + float(t_d)
            new_data_file.write(str(v))
            new_data_file.write(' ')
            row_count += 1
        line_count += 1
        new_data_file.write('\n')

    new_data_file.close()
    stand_file.close()
    test_file.close()

if __name__ == '__main__':
    main()