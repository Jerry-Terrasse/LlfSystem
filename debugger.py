from PIL import ImageGrab as ig
import time
import cv2 as cv
import numpy as np
import surgeon as sgn

def tk():
    for i in range(11):
        ig.grab((640,680,695,700)).save(str(i)+".png")
        time.sleep(3)

def showimg(str):
    img=cv.imread(str,0)
    ret,img=cv.threshold(img,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.namedWindow('1',cv.WINDOW_AUTOSIZE)
    cv.imshow('1',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def collect(wait=1):
    sgn.get_ori()
    while True:
        cv.imwrite("D:/"+time.asctime().replace(':','_').replace(' ','_')+".png",sgn.get_image("whole"))
        time.sleep(wait)
    return