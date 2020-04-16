'''
Get darknet dataset information class wise
data_path  = dataset path
'''

import os
import sys
import cv2
import glob

num_class = 4
data_path = sys.argv[1]

classes = {}
for i in range(num_class):
    classes[i] = 0

data_files = glob.glob(os.path.join(data_path,'*.txt'))

for txt_file in data_files:
    f = open(txt_file,'r')
    for line in f:
        numbers = [float(num) for num in line.split()]
        numbers[0] = int(numbers[0])
        classes[numbers[0]] = classes[numbers[0]] + 1

print("Total classes:{}".format(classes))
