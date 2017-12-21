from svmutil import *
import sys

# same to train_data.py
file_model_name = "model_file"

# file of test data
file_test_name = sys.argv[1]
label, data = svm_read_problem(file_test_name)

model = svm_load_model(file_model_name)
p_labels, p_acc, p_vals = svm_predict(label, data, model)
print p_labels
print p_acc
print p_vals
