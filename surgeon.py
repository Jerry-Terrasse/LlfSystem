from teleporter import *
from matcher import *
from shoter import *
import time


orix=int()
oriy=int()
to_ori=(-344,-313)

poslib={
    'bottom_lef': (176, 507), 'bottom_rig': (196, 507),
    'card_0': (121, 604), 'card_1': (191, 604), 'card_2': (261, 604), 'card_3': (331, 604),
    'water_sta': (104,640), 'water_end': (124, 660),
    'bridge_lef': (89, 208), 'bridge_rig': (289, 208),
    'opp_lit_lef': (89, 153), 'opp_lit_rig': (289, 153),
    'opp_bld_lef_sta': (75, 102), 'opp_bld_lef_end': (114, 103),
    'opp_bld_rig_sta': (275, 102), 'opp_bld_rig_end': (314, 103),
    'fight':(125,440),'sure':(190,600),
    'whole_sta':(0,0),'whole_end':(381,677)
}


def get_ori():
    global orix,oriy
    shot("cur_screen.png")
    orix,oriy=match_pos("cur_screen.png","Sources/core.png")
    orix+=to_ori[0]
    oriy+=to_ori[1]
    print("Ori Token: ("+str(orix)+","+str(oriy)+")")

def display_bypos(card,desx,desy):
    click(orix+poslib[card][0],oriy+poslib[card][1])
    time.sleep(0.2)
    click(orix+desx,oriy+desy)

def display_byname(card,name):
    click(orix+poslib[card][0],oriy+poslib[card][1])
    time.sleep(0.2)
    click(orix+poslib[name][0],oriy+poslib[name][1])

def get_vector():
    curx,cury=get_pos()
    return curx-orix,cury-oriy

def get_image(which,flg=""):
    shot(which+flg+".png",orix+poslib[which+'_sta'][0],oriy+poslib[which+'_sta'][1],orix+poslib[which+'_end'][0],oriy+poslib[which+'_end'][1])

def next_fight():
    click(orix+poslib['sure'][0],oriy+poslib['sure'][1])
    time.sleep(3)
    click(orix+poslib['fight'][0],oriy+poslib['fight'][1])
    time.sleep(10)


if __name__=='__main__':
    print("Surgeon Here")
