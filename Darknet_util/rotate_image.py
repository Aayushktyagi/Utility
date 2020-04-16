'''
-> load images and txt file
-> rotate image
-> rotate coordinates
'''
import os
import sys
import glob
import cv2
import numpy as np

# globale variable
bb ={}
new_bb = {}
file_counter = 0


def get_coord_list(wi,hi,coord):
    '''
    input : [xc,yc,w,h]
    output :get all (x,y) coordinates:[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
    '''
    # wi,hi = img.shape[:2]
    coord = coord[1:]
    coord[0] = coord[0]* hi
    coord[1] = coord[1]* wi
    coord[2] = coord[2] * hi
    coord[3] = coord[3] * wi
    xmin = coord[0] - coord[2]/2
    ymin = coord[1] - coord[3]/2
    width = coord[2]
    height = coord[3]
    x1 = xmin - width/2
    y1 = ymin - height/2
    x2 = x1 + width
    y2 = y1
    x3 = x1 + width
    y3 = y1 + height
    x4 = x1
    y4 = y1+height

    new_coord = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
    return new_coord

def get_coord(file):
    '''
    get coordinates from txt file
    '''
    coordinates = []
    with open(file) as f:
        for line in f:
            numbers = [float(num) for num in line.split()]
            coordinates.append(numbers)

    f.close()
    return coordinates

def show_coord(coord,img):
    '''
    Show image and coordinates
    '''
    real_img = img.copy()
    box_color = 110,255,0
    #image shape
    wi,hi = img.shape[:2]
    for coord in coordinates:
        coord = coord[1:]
        xC = coord[0]* hi
        yC = coord[1]* wi
        w = coord[2] * hi
        h = coord[3] * wi
        cv2.rectangle(img , (int(xC-w/2),int(yC-h/2)),(int(xC+w/2),int(yC+h/2)),box_color,2)

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    return real_img
def rotate_image(image, angle):
    '''
    rotate image with angle
    '''

    # grab the dimensions of the image and then determine the
    # centre
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def rotate_box(bb, cx, cy, h, w):
    '''
    rotate coordinates
    '''
    print("bounding_box",bb)
    theta = 45
    new_bb = list(bb)
    for i,coord in enumerate(bb):
        # opencv calculates standard transformation matrix
        M = cv2.getRotationMatrix2D((cx, cy), theta, 1.0)
        # Grab  the rotation components of the matrix)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cx
        M[1, 2] += (nH / 2) - cy
        # Prepare the vector to be transformed
        v = [coord[0],coord[1],1]
        # Perform the actual rotation and return the image
        calculated = np.dot(M,v)
        new_bb[i] = (calculated[0],calculated[1])
    return new_bb
#image path
folder_path = sys.argv[1]

#load images and txt files
files = glob.glob(os.path.join(folder_path,'*.jpg'))

for img in files:
    file_counter = file_counter+1
    print("File counter :{}".format(file_counter))
    #img file
    image = cv2.imread(img)
    #txt file name
    txt_filename =os.path.splitext(os.path.basename(img))[0] + '.txt'
    txt_filepath = os.path.join(folder_path,txt_filename)
    coordinates = get_coord(txt_filepath)
    print("Coordinates :{}".format(coordinates))
    #show image
    # image = show_coord(coordinates,image)
    rotated_image = rotate_image(image,45)
    #rotate coordinates
    # Calculate the shape of rotated images
    (heigth, width) = image.shape[:2]
    (cx, cy) = (width // 2, heigth // 2)
    (new_height, new_width) = rotated_image.shape[:2]
    (new_cx, new_cy) = (new_width // 2, new_height // 2)
    print(cx,cy,new_cx,new_cy)
    for coord in coordinates:
        print("coord",coord)
        coord_list = get_coord_list(width,heigth,coord)
        print("coord_list",coord_list)
        new_bb = rotate_box(coord_list, cx, cy, heigth, width)
    print(new_bb[0])
    cv2.rectangle(rotated_image,(int(new_bb[0][0]),int(new_bb[0][1])),(int(new_bb[2][0]),int(new_bb[2][1])),(110,255,0),2)
    cv2.imshow('image',rotated_image)
    cv2.waitKey(0)
