from svmutil import *
import sys
import time
from pixels import Pixels, pixels
from google_home_led_pattern import GoogleHomeLedPattern


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
acc = int(p_acc[0])

if acc == 100:
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show, color=1)
else:
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show, color=2)

while True:
    try:
        pixels.speak()
        time.sleep(6)
    except KeyboardInterrupt:
        break

pixels.off()
time.sleep(1)



