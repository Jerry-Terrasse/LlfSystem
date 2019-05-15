from surgeon import *
from regulator import *
from decoder import *
from random import randint
import time
# from teleporter import *
# from matcher import *


def herewego():
    if randint(0,1):
        display_byname('card_'+str(randint(0,3)),'bottom_lef')
    else:
        display_byname('card_'+str(randint(0,3)),'bottom_rig')


def Awave():
    ban=randint(0,3)
    if randint(0,1):
        position='opp_lit_lef'
    else:
        position='opp_lit_rig'
    for i in range(4):
        if i!=ban:
            display_byname('card_'+str(i),position)

def Defend():
    ban=randint(0,3)
    if randint(0,1):
        position='bottom_lef'
    else:
        position='bottom_rig'
    for i in range(4):
        if i!=ban:
            display_byname('card_'+str(i),position)

if __name__=='__main__':
    print("LLF AK IOI !!!")
    fight_start()
    while True:
        water=get_water()
        print(water,"WATERs now")
        if water>=9:
            if Fight():
                if water<10:
                    time.sleep(1)
                Awave()
            else:
                Defend()
        time.sleep(1.5)