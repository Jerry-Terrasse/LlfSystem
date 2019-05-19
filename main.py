from surgeon import *
import regulator as rgr
from decoder import *
from random import randint
import time
import sys
# from teleporter import *
# from matcher import *

AUTO=False

def herewego():
    if randint(0,1):
        display_byname('card_'+str(randint(0,3)),'bottom_lef')
    else:
        display_byname('card_'+str(randint(0,3)),'bottom_rig')


def Awave():
    rgr.set_pre_time()
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
    if rgr.started:
        display_bypos('card_'+str(randint(0,3)),posx,posy+50)
    '''
    for i in range(4):
        if i!=ban:
            # display_byname('card_'+str(i),position)
            display_bypos('card_'+str(i),posx,posy)
    '''

if __name__=='__main__':
    if len(sys.argv)>1:
        AUTO=True
    print("LLF AK IOI !!! && LJH AK IMO!!!")
    rgr.fight_start()
    get_ori()
    while True:
        water=get_water()
        if not rgr.started:
            if AUTO:
                next_fight()
                rgr.fight_start()
                continue
            else:
                exit()
        bld_lef=get_bld("opp_bld_lef")
        bld_rig=get_bld("opp_bld_rig")
        print("%d WATER; %.2f%% LEFT; %.2f%% RIGHT;" % (water,bld_lef*100/38,bld_rig*100/38))
        if water>=4:
            Defend()
        time.sleep(1.5)