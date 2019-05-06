from teleporter import *
from PIL import ImageGrab
import time

# posx=(644,713,775,875)
# posy=(644,644,644,644)
posx=(-223,-153,-83,-13)
posy=291
orix=int()
oriy=int()

def get_ori():
  ImageGrab.grab().save("cur_screen.png")
  orix,oriy=match("cur_screen.png","Sources/core.png")

def display(id,desx,desy):
  click(posx[id],oriy+posy)
  time.sleep(0.1)
  click(desx,desy)

if __name__=='__main__':
  print("Surgeon Here")
