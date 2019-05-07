from teleporter import *
from matcher import *
from PIL import ImageGrab
import time

# posx=(644,713,775,875)
# posy=(644,644,644,644)
posx=(-223,-153,-83,-13)
posy=291
orix=int()
oriy=int()
poslib={'bottom_lef':(-168,194),'bottom_rig':(-148,194)}

def get_ori():
  global orix,oriy
  ImageGrab.grab().save("cur_screen.png")
  orix,oriy=match("cur_screen.png","Sources/core.png")

def display_bypos(id,desx,desy):
  click(orix+posx[id],oriy+posy)
  time.sleep(0.1)
  click(desx,desy)

def display_byname(id,name):
  click(orix+posx[id],oriy+posy)
  time.sleep(0.1)
  click(orix+poslib[name][0],oriy+poslib[name][1])

if __name__=='__main__':
  print("Surgeon Here")
