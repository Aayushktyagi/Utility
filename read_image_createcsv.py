'''
Read images from multiple sub-folders(ex:0,1,2,3,....)
create a csv file with format filename , label
filenmae being name of image and label being folder name
move images to folder names as destination folder
max 200 images from each folder can be added 
images added will me moved to destination folder specified with destination path
'''

import pandas as pd
import os
import sys
import shutil

train_path = 'path to dataset'
destination_path = 'path to destination folder'

def getcsv(datapath , train=True):
    filename_list = []
    label_list = []
    label_counter_dict = {}
    for root, dirs, files in os.walk(datapath):
        for f in files:
            if f.endswith(".jpg"):
                label = os.path.basename(root)
                if label not in label_counter_dict.keys() :
                    label_counter_dict[label] = 0
#                     print(label_counter_dict)
                    filename_list.append(f)
                    label_list.append(label)
                    image_path = os.path.join(root,f)
                    path = shutil.copy(image_path,destination_path)
                    if os.path.isfile(path):
                        pass
#                     print("")
                    else:
                        print("file does not exist")
                        break
                else:

                    if label_counter_dict[label] <=200:
                        label_counter_dict[label] = label_counter_dict[label] + 1
                        filename_list.append(f)
                        label_list.append(label)
                        image_path = os.path.join(root,f)
                        path = shutil.copy(image_path,destination_path)
                        if os.path.isfile(path):
                            pass
#                     print("")
                        else:
                            print("file does not exist")
                            break
                
                
    print(label_counter_dict)
    df = pd.DataFrame(list(zip(filename_list, label_list)), 
               columns =['filename', 'label']) 
    print(df.head())
    if train:
        print('saving train csv file')
        df.to_csv('train.csv',index=False)
    else:
        print("savig test csv file")
        df.to_csv('test.csv',index=False)
            
getcsv(combined_cam2)