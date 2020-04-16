'''
remove txt files that are empty

'''


import os
import sys
import glob

folder_path = sys.argv[1]

files = glob.glob(os.path.join(folder_path,'*.txt'))

for file in files:
    basename = os.path.splitext(os.path.basename(file))[0]
    image_path = folder_path +  str(basename) + '.jpg'
    if os.path.exists(image_path):
        if os.path.getsize(file) ==0:
            os.remove(image_path)
            os.remove(file)
            print("Removing file:{}".format(image_path))
    else:
        print("File does not exits")
