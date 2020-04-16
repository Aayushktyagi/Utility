'''
load txt file and extract/crop images of particular class
crop_class = index of class to be cropped

'''

import os
import sys
import cv2
import argparse
import parser
import glob
import uuid
import numpy as np

def convert_yolo_cart(numbers,width,height):
    coord = numbers[1:]
    coord[0] = coord[0] * height
    coord[1] = coord[1] * width
    coord[2] = coord[2] * height
    coord[3] = coord[3] * width
    xmin = int(coord[0] - coord[2]/2)
    ymin = int(coord[1] - coord[3]/2)
    xmax = int(coord[0] + coord[2]/2)
    ymax = int(coord[1] + coord[3]/2)

    return xmin,ymin,xmax,ymax

def process(args):
    data_path = args.input
    output_path = args.output
    data_files = glob.glob(os.path.join(data_path,'*.txt'))
    # crop_class = args.class
    crop_class = 0
    count = 0
    for txt_file in data_files:
        count = count + 1
        print("Counter:{}".format(count))
        #load image
        basename = os.path.splitext(os.path.basename(txt_file))[0]
        image_name = basename + '.jpg'
        image_path = os.path.join(data_path,image_name)
        image = cv2.imread(image_path)
        try:
            width , height = image.shape[:2]
        except:
            print("Image with None type")
            continue
        f = open(txt_file,'r')
        for line in f:
            name_uuid = uuid.uuid4().int
            numbers = [float(num) for num in line.split()]
            if int(numbers[0]) == crop_class:
                try:
                    xmin,ymin,xmax,ymax = convert_yolo_cart(numbers,width,height)
                    crop_img = image[ymin:(ymax+10),xmin:xmax]
                    crop_img = cv2.resize(crop_img,(250,300))
                    # cv2.imshow("cropeed image",crop_img)
                    cv2.imwrite(os.path.join(output_path,str(name_uuid)+'.jpg'),crop_img)
                    # cv2.waitKey(0)
                except:
                    print("Error in :{}".format(txt_file))
                    continue
            else:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',help='path to dataset',required = True)
    parser.add_argument('--class',help = 'Class to crop',type = int , required = True)
    parser.add_argument('--output',help = 'path to write data ',required = True)
    args = parser.parse_args()
    process(args)
