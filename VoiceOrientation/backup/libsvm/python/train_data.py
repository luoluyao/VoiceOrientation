from svmutil import *

# file to save model
file_model_name = "model_file"

# file of training data
file_training_name = "newlog_merge_1"
label, data = svm_read_problem(file_training_name)


# -s  2 -- one-class SVM
# -t 2 -- radial basis function: exp(-gamma*|u-v|^2)
# -n 0.5 default
model = svm_train(label, data, '-s 0 -t 1 -n 0.5')
svm_save_model(file_model_name, model)
p_labels, p_acc, p_vals = svm_predict(label, data, model)
print p_labels
print p_acc
print p_vals
