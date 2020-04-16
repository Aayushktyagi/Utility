'''
load multiple images and create txt file fir each of them

'''
import sys
import os
import cv2

folder_path = sys.argv[1]
images = []
for root , _ ,  files in os.walk(folder_path):
    current_directory_path = os.path.abspath(root)
    for f in files:
        name ,ext = os.path.splitext(f)
        if os.path.exists(os.path.join(current_directory_path,f)):
            current_image_path = os.path.join(current_directory_path,f)
            current_txt_path = os.path.join(current_directory_path,name+'.txt')
            f = open(current_txt_path,'a')
            data = ' '
            f.write(data + "\n")
            f.close()
