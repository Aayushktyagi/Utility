'''
path = path of base directory
read all images in all subfolders from base directory
'''
def getImages(path):
    images = []
    for root , folder , filename in os.walk(path):
        for f in filename:
            file = os.path.join(root,f)
            if f.endswith(".jpg"):
                img = cv2.imread(file)
                if img is not None:
                    images.append(img)
    return images