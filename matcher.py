# Reference from http://bluewhale.cc/2017-09-22/use-python-opencv-for-image-template-matching-match-template.html

import cv2

def match(image,target):
  img=cv2.imread(image,0)
  tar=cv2.imread(target,0)
#  res=cv2.matchTemplate(img,tar,cv2.TM_SQDIFF_NORMED)
  res=cv2.matchTemplate(img,tar,cv2.TM_CCOEFF_NORMED)
  res=cv2.minMaxLoc(res)
  res=res[3]
  return res

if __name__=='__main__':
  print("Matcher Here")