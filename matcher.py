# Reference from http://bluewhale.cc/2017-09-22/use-python-opencv-for-image-template-matching-match-template.html

import cv2
import numpy as np

def simularity(image,target):
    img=cv2.imread(image,0)
    tar=cv2.imread(target,0)
    img=get_two(img)
    tar=get_two(tar)
    ret=cv2.compare(img,tar,cv2.CMP_EQ)
    ret=np.sum(ret)
    return ret

def match(image,target):
    img=cv2.imread(image,0)
    tar=cv2.imread(target,0)
#    ret=cv2.matchTemplate(img,tar,cv2.TM_SQDIFF_NORMED)
    ret=cv2.matchTemplate(img,tar,cv2.TM_CCOEFF_NORMED)
    ret=cv2.minMaxLoc(ret)
    return ret

def match_pos(image,target):
    return match(image,target)[3]

def match_val(image,target):
    return match(image,target)[1]

def get_arr(image,through=None):
    ret=cv2.imread(image)
    if not through is None:
        ret=ret[:,:,through]
    return ret

def get_two(img,thresh=None):
    if thresh is None:
        ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    else:
        ret,img=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
    # ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE)
    return img

def match_diff(image,target):
    img=get_arr(image)
    tar=get_arr(target)
    ret=img
    x,y,z=img.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                a=int(img[i][j][k])-int(tar[i][j][k])
                if a<100 and a>-100:
                    ret[i][j][k]=0
                else:
                    ret[i][j][k]=255
    return ret

if __name__=='__main__':
    print("Matcher Here")