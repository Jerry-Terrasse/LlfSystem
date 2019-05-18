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
    set_pre_time()
    time.sleep(1)
    ban=randint(0,3)
    if bld_lef<bld_rig:
        position='opp_lit_lef'
    else:
        position='opp_lit_rig'
    for i in range(4):
        if i!=ban:
            display_byname('card_'+str(i),position)

def Defend():
    '''
    ban=randint(0,3)
    if randint(0,1):
        position='bottom_lef'
    else:
        position='bottom_rig'
    '''
    posx,posy=war_at()
    display_bypos('card_'+str(randint(0,3)),posx,posy)
    '''
    for i in range(4):
        if i!=ban:
            # display_byname('card_'+str(i),position)
            display_bypos('card_'+str(i),posx,posy)
    '''

if __name__=='__main__':
    print("LLF AK IOI !!!")
    fight_start()
    while True:
        water=get_water()
        bld_lef=get_bld("opp_bld_lef")
        bld_rig=get_bld("opp_bld_rig")
        print("%d WATER; %.2f%% LEFT; %.2f%% RIGHT;" % (water,bld_lef*100/38,bld_rig*100/38))
        # print(water,"WATER;",str(bld_lef*100/38)+'%',"LEFTBLOOD")
        if Fight():
            if water>=9:
                Awave()
        elif water>=4:
            Defend()
        '''
        if water>=8:
            if Fight():
                Awave()
            else:
                Defend()
        '''
        time.sleep(1.5)