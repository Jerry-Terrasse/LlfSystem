import surgeon as sgn
import regulator as rgr
import decoder as dcd
import polician as plc
from random import randint
import time
import sys


AUTO=False
water=int()
bld_lef=int()
bld_rig=int()
card_inf=int()


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
        sgn.display_bypos('card_'+str(randint(0,3)),posx,posy+30)
    elif water>=8:
        if bld_lef<bld_rig:
            position='bottom_lef'
        else:
            position='bottom_rig'
        sgn.display_byname('card_'+str(randint(0,3)),position)


if __name__=='__main__':
    if len(sys.argv)>1:
        AUTO=True
    print("LLF AK IOI !!!")
    dcd.load_images()
    rgr.fight_start()
    sgn.get_ori()
    while True:
        bld_lef=dcd.get_bld("opp_bld_lef")
        bld_rig=dcd.get_bld("opp_bld_rig")
        card_inf = dcd.get_card()
        if bld_lef<0:
            out_bld_lef="DESTROYED;"
            bld_lef=100
        else:
            out_bld_lef="%.2f%% LEFT;" % (bld_lef*100/38)
        if bld_rig<0:
            bld_rig=100
            out_bld_rig="DESTROYED;"
        else:
            out_bld_rig="%.2f%% RIGHT;" % (bld_rig*100/38)
        print(out_bld_lef,out_bld_rig)
        # print("%d WATER; %.2f%% LEFT; %.2f%% RIGHT;" % (water,bld_lef*100/38,bld_rig*100/38))
        water=dcd.get_water()
        if not rgr.started:
            if AUTO:
                sgn.next_fight()
                rgr.fight_start()
                continue
            else:
                exit()
        '''
        out_water="%d WATER;" % (water)
        print()
        print(out_water,out_bld_lef,out_bld_rig)
        out_card = "CARD: "
        for i in card_inf:
            out_card += i + '; '
        print(out_card)
        '''
        plc.meeting(water,bld_lef,bld_rig,card_inf)
        time.sleep(1)