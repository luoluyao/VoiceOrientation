import sys
import string

def count_legal(standard_data, test_data, thr):
    legal_count = 0
    for i in range(3):
        for j in range(4):
            if (abs(abs(string.atof(standard_data[i][j])) - abs(string.atof(test_data[i][j]))) < thr):
                legal_count +=1
            else:
                print ":", i, j, test_data[i][j]
    return legal_count

def main():
    # threshold for statistics
    thr = 10 # mm
    result_data = 0
    result_all_data = 0
    # groundtruth data file
    standardFile = sys.argv[1]
    # test data file
    testFile = sys.argv[2]

    stand_file = open(standardFile)
    stand_data = stand_file.readlines()
    # groundtruth data array
    stand_datas = []
    for s_data in stand_data:
        d = s_data.strip('\n').split(" ")
        stand_datas.append(d)

    test_file = open(testFile)
    test_data = test_file.readlines()
    count = 0
    all_count = 0
    test_datas = []
    for t_data in test_data:
        t = t_data.strip('\n').split(",")
        test_datas.append(t)
        count += 1
        result_all_data += 4
        if count == 3:
            count = 0
            all_count += 1
            print "num:", all_count
            result_data += count_legal(stand_datas, test_datas, thr)
            test_datas = []
    print result_data, result_data / float(result_all_data)
    stand_file.close()
    test_file.close()

if __name__ == '__main__':
    main()