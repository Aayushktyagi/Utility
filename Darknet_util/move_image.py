'''
Move n number of images with txt files from
one folder to another
'''
import sys
import os
import shutil
import glob
#target path
target_path = '/home/aayush/Downloads/Vision/Video/Dataset/person_data_cctv/1/15_hundred_img_person'
destination_path = os.getcwd() + '/temp_data'
print("destination_path",destination_path)

#number of images
count = 10

file_counter = 0
#get image list
image_list = glob.glob(os.path.join(target_path,'*.jpg'))
for image in image_list:
    print(file_counter)
    basename = os.path.splitext(os.path.basename(image))[0]
    txt_filename = os.path.join(target_path,basename+'.txt')
    if file_counter < 10:
        # print()
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
            if os.path.exists(txt_filename):
                shutil.copy(image , destination_path)
                shutil.copy(txt_filename,destination_path)
                file_counter = file_counter + 1
            else:
                pass
        else:
            if os.path.exists(txt_filename):
                shutil.copy(image,destination_path)
                shutil.copy(txt_filename,destination_path)
                file_counter = file_counter + 1
            else:
                pass
