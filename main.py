from surgeon import *
from regulator import *
from random import randint
# from teleporter import *
# from matcher import *



if __name__=='__main__':
  print("LLF AK IOI !!!")
  fight_start()
  while True:
    if randint(0,1):
      display_byname(randint(0,3),'bottom_lef')
    else:
      display_byname(randint(0,3),'bottom_rig')
    wait()