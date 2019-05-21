import surgeon as sgn
import regulator as rgr
import decoder as dcd
from random import randint
import time
import sys


AUTO=False
water=int()
bld_lef=int()
bld_rig=int()


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
            sgn.display_byname('card_'+str(i),position)

def Defend():
    global water,bld_lef,bld_rig
    posx,posy=dcd.war_at()
    if posx or posy:
        sgn.display_bypos('card_'+str(randint(0,3)),posx,posy+50)
    elif water>=9:
        if bld_lef<bld_rig:
            position='bottom_lef'
        else:
            position='bottom_rig'
        sgn.display_byname('card_'+str(randint(0,3)),position)


if __name__=='__main__':
    if len(sys.argv)>1:
        AUTO=True
    print("LLF AK IOI !!! && LJH AK IMO!!!")
    rgr.fight_start()
    sgn.get_ori()
    while True:
        water=dcd.get_water()
        if not rgr.started:
            if AUTO:
                sgn.next_fight()
                rgr.fight_start()
                continue
            else:
                exit()
        bld_lef=dcd.get_bld("opp_bld_lef")
        bld_rig=dcd.get_bld("opp_bld_rig")
        print("%d WATER; %.2f%% LEFT; %.2f%% RIGHT;" % (water,bld_lef*100/38,bld_rig*100/38))
        if water>=4:
            Defend()
        time.sleep(1.5)