'''
Check for perticualr class in txt files
If present then move to another folder

'''

import os
import sys
import numpy
import cv2
import argparse
import glob
import uuid
import shutil

def process(args):
    data_path = args.input
    destination_path = args.output
    data_files = glob.glob(os.path.join(data_path,'*.txt'))
    # crop_class = args.class
    crop_class = 2
    for txt_file in data_files:
        #load image
        image_basename  = os.path.splitext(os.path.basename(txt_file))[0]
        image_name = image_basename + '.jpg'
        image = os.path.join(data_path,image_name)
        # print(image)
        move_status = 0
        f = open(txt_file,'r')
        for line in f:
            numbers = [float(num) for num in line.split()]
            if int(numbers[0]) == crop_class:
                #file need to be moved
                move_status = 1
        if move_status == 1:
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)
                if os.path.exists(txt_file):
                    print("Coping file:{}".format(image))
                    shutil.copy(image , destination_path)
                    shutil.copy(txt_file,destination_path)
                else:
                    pass
            else:
                if os.path.exists(txt_file):
                    print("Coping file:{}".format(image))
                    shutil.copy(image,destination_path)
                    shutil.copy(txt_file,destination_path)
                else:
                    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',help='path to dataset',required = True)
    parser.add_argument('--class',help = 'Class to crop',type = int , required = True)
    parser.add_argument('--output',help = 'path to write data ',required = True)
    args = parser.parse_args()
    process(args)
