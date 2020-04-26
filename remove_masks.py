'''
check files in train remove files from annotation if file not present in images
'''
import os
import sys
import shutil

check_count = 0
image_count = 0
image_list =[]
root_dir = sys.argv[1]

images_dir = os.path.join(root_dir,'Refinedimages')
annot_dir = os.path.join(root_dir,'Refined_annot')

for root,dirs,files in os.walk(annot_dir):
    for f in files:
        # print(os.path.join(images_dir,f))
        if os.path.isfile(os.path.join(images_dir,f)):
            image_count+=1
        else:
            # print("file not present")
            check_count +=1
            shutil.move(os.path.join(annot_dir,f),os.path.join(root_dir,'extra_annot'))
            #move annot to temp dir




print("Number of moved files:{}".format(check_count))
print("Image count:{}".format(image_count))
