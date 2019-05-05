from teleporter import *
import time

posx=(644,713,775,875)
posy=(644,644,644,644)

def display(id,desx,desy):
  click(posx[id],posy[id])
  time.sleep(0.1)
  click(desx,desy)
