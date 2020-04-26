# Utility
Small utility scripts
1. Reading_recursive_images.py:read all images in all subfolders from base directory
2. Darknet Utility scripts:
   1. create_neg.py:load multiple images and create txt file for each of them
   2. create_train.py:collect txt files from folder and write x% of files to train.txt
      and rest(1-x)% to valid.txts.
   3. dataset_info.py:Get darknet dataset information class wise
   4. get_class_and_move.py:Check for perticualr class in txt files.If present then move to another folder
   5. load_n_crop.py:load txt file and extract/crop images of particular class
   6. move_image.py:Move n number of images with txt files from one folder to another
   7. read_and_replace_txt.py:load txt files and replace first charater to 0
   8. remove_txt.py:remove txt files that are empty
   9. rename_and_move.py:File to rename files with uuid and copy into another folder
   10. rotate_image.py:rotate image and rotate coordinates
3. Remove mask:check files in train remove files from annotation if file not present in images
  
