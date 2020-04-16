'''
File to rename files with uuid and copy into another folder
'''

import os
import sys
import uuid
import glob
'''
mode = 1: rename
mode = 2: copy
'''
file_path = sys.argv[1]

image_list = glob.glob(os.path.join(sys.argv[1],'*.jpg'))
for image in image_list:
    name_uuid = uuid.uuid4().int
    basename = os.path.splitext(os.path.basename(image))[0]
    txt_filename = os.path.join(file_path,basename+'.txt')
    if os.path.exists(image):
        if os.path.exists(txt_filename):
            uuid_image = os.path.join(file_path,str(name_uuid)+'.jpg')
            uuid_text = os.path.join(file_path,str(name_uuid)+'.txt')
            os.rename(image,uuid_image)
            os.rename(txt_filename,uuid_text)
        else:
            print("File does not exists:{}".format(txt_filename))
    else:
        print("image does not exists:{}".format(image))
