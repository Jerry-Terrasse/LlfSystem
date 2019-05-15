# Reference from http://bluewhale.cc/2017-09-22/use-python-opencv-for-image-template-matching-match-template.html

import cv2
import numpy as np

def simularity(image,target):
    img=cv2.imread(image,0)
    tar=cv2.imread(target,0)
    ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    ret,tar=cv2.threshold(tar,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
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

if __name__=='__main__':
    print("Matcher Here")