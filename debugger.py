from PIL import ImageGrab
import time
import cv2
import numpy as np

def tk():
    for i in range(11):
        ImageGrab.grab((640,680,695,700)).save(str(i)+".png")
        time.sleep(3)

def showimg(str):
    img=cv2.imread(str,0)
    ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    cv2.namedWindow('1',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('1',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def asdf():
    img=cv2.imread("whole0.png")
    tar=cv2.imread("whole1.png")
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