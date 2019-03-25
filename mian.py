import cv2
import os

rootpath = 'G:/VOC2012/SegmentationClass'
outpath = 'G:/VOC2012/zk'

for filename in os.listdir(rootpath):
    print(filename)
    print(rootpath+'/'+filename)
    img = cv2.imread(rootpath+'/'+filename)
    size = img.shape
    for i in range(size[0]):
        for j in range(size[1]):
            if(img[i,j,0]!=128 or img[i,j,1]!=128 or img[i,j,2]!=192):
                img[i,j,0] = 0
                img[i,j,1] = 0
                img[i,j,2] = 0

    cv2.imwrite(outpath+'/'+filename,img)