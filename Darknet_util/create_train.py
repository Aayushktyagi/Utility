'''
collect txt files from folder and write x% of files to train.txt
and rest(1-x)% to valid.txts

'''
#Input arguments
#folder name
#train data percentage
#collect all txt files
#collect all images format
import argparse
import sys
import os
import getopt
import numpy
import cv2
import glob
import random
import collections
import shutil
#config paramters:
check_txt = 1
check_txt_image_count = 1
create_train_valid_file = 1
remove_file = 0
train_valid_txt_file_path = '/home/aayush/Downloads/Vision/Video/Dataset/Test/'
source_folder ='/opt/github/dataset/fire_smoke/fire_img_20_11_18/'
destination_folder = '/opt/github/dataset/fire_smoke/fire_dataset/'
def match(txt_list,image_list):
    print(len(txt_list),len(image_list))
    if len(txt_list) == len(image_list):
        print("Equal number of files:{}".format(len(txt_list)))
    else:
        print("File counter miss match image_list {}: txt_list {}".format(len(image_list),len(txt_list)))
    #check for elements in list
    if collections.Counter(txt_list) == collections.Counter(image_list):
        print("Equal element wise ")
    else:
        print("File mis-match")
    #get uncommon files:
    mis_match_files_i2t = list(set(image_list) - set(txt_list))
    mis_match_files_t2i = list(set(txt_list)-set(txt_list))
    print("mis matched Files:",mis_match_files_i2t,mis_match_files_t2i)
    mis_match_files = mis_match_files_t2i or  mis_match_files_i2t
    print("Final list:{}".format(mis_match_files))
    return mis_match_files

def txt_format(file):
    print("Filename:",file)
    with open(file , mode='r+') as f:
        for line in f:
            numbers = [float(num) for num in line.split()]

            #check
            print("data:{}".format(numbers))
            if numbers!=[]:
                print("data:{}".format(numbers))
                coord = numbers[1:]
                if all(i <= 1 for i in coord):
                    pass
                elif all(i >= 1 for i in coord):
                    raise Exception("coordinates value greater that 1 : Please check")
                else:
                    raise Exception("Coordinate value miss matcch: plase check line {}".format(cnt))
                #check class
                label = numbers[0]
                print("label:{}".format(label))
                if label != 0:
                    f.write(line.replace('1','0',1))
                    raise Exception("label does not match :Please check ")
                return 1
            else:
                return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Add annotation to train and valid')
    parser.add_argument('--folder' , type=str)
    parser.add_argument('--split',type=float , default = 98.0)

    args = parser.parse_args()

    #collect images and txt files in folder
    try:
        image_counter = 0
        txt_counter = 0
        match_counter = 0
        txt_list = []
        image_list =[]
        files_grabbed_txt = glob.glob(os.path.join(args.folder,'*.txt'))
        files_grabbed_images =[]
        for ext in ('*.JPEG','*.jpg','*.png'):
            files_grabbed_images.extend(glob.glob(os.path.join(args.folder,ext)))
        print("images files :",files_grabbed_images)
        print("number of text files:{}".format(len(files_grabbed_txt)))
        print("number of images:{}".format(len(files_grabbed_images)))
        #check txt files for irrigularity:
        if check_txt ==1:
            for file in files_grabbed_txt:
                status = txt_format(file)
                if status ==1:
                    txt_counter = txt_counter+1
                    basename = os.path.basename(file)
                    file_name = os.path.splitext(basename)[0]
                    txt_list.append(file_name)
                else:
                    txt_counter = txt_counter+1
                    basename = os.path.basename(file)
                    file_name = os.path.splitext(basename)[0]
                    txt_list.append(file_name)
        if check_txt_image_count ==1:
            print("files")
            for file in files_grabbed_images:
                image_counter = image_counter+1
                basename = os.path.basename(file)
                file_name = os.path.splitext(basename)[0]
                image_list.append(file_name)
            print("starting matching ")
            mis_match_files=match(txt_list,image_list)
            print("miss_match files:{}".format(len(mis_match_files)))
            if len(mis_match_files) == 0:
                print("Starting spliting data")
                #check create train valid txt file
                if create_train_valid_file ==1:
                    num_images = len(image_list)
                    train_split = int(0.01*args.split*num_images)
                    print("train size:{}".format(train_split))
                    print("index before shuffle:{}".format(image_list[0]))
                    random.shuffle(files_grabbed_images)
                    print("index after shuffle:{}".format(image_list[0]))
                    #add files to train.txt
                    if create_train_valid_file ==1:
                        f = open(train_valid_txt_file_path+"train.txt",'a')
                        for i in range(0,train_split):
                            print("Writing image:",files_grabbed_images[i])
                            f.write(files_grabbed_images[i] + '\n')
                        v = open(train_valid_txt_file_path+"valid.txt","a")
                        for i in range(train_split,len(image_list)):
                            v.write(files_grabbed_images[i] + '\n')
            else:
                print("mis match files:{}".format(mis_match_files))
        if remove_file==1:
            #get txt files:
            for files in files_grabbed_txt:
                shutil.copy(files, destination_folder)
            txt_folder = glob.glob(os.path.join(destination_folder,'*.txt'))
            img_folder = glob.glob(os.path.join(args.folder,'*.jpg'))
            copy_couter = 0
            txt_counter  = 0
            for txt_file in txt_folder:
                txt_counter = txt_counter+1
                #base filename;
                txt_orignal = txt_file
                filename = os.path.basename(txt_file)
                filename_txt = os.path.splitext(filename)[0]

                for img_name in img_folder:
                    img_orignal = img_name
                    #compare image
                    filename_img = os.path.basename(img_name)
                    filename_img = os.path.splitext(filename_img)[0]
                    if filename_txt == filename_img:
                        print("Image copied:{}".format(img_orignal))
                        shutil.copy(img_orignal,destination_folder)
                        copy_couter = copy_couter+1
            print("number of files copied:{}".format(copy_couter))
            print("number of files txt files:{}".format(txt_counter))



    except Exception as e:
        print("Error in loading dataset:",str(e))
