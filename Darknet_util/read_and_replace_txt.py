'''
load txt files and replace first charater to 0
'''
import sys
import glob
import os



filepath = sys.argv[1]
files = glob.glob(os.path.join(filepath,'*.txt'))

#read file
for file_name in files:
    filedata = None
    with open(file_name , 'r') as f:
        filedata = f.readlines()
        print(filedata[0])
        with open(file_name,'w+') as f2:
            for lines in filedata:
                if lines !='':
                    first_data = '0'
                    rest_char = lines[1:]
                    all_char = first_data+rest_char
                    print(all_char)
                    f2.write(all_char+"\n")
