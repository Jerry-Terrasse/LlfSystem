import teleporter as  tp
import matcher as mtr
import shoter as shtr
import time


orix=int()
oriy=int()
to_ori=(-344,-313)

poslib={
    'bottom_lef': (175, 505), 'bottom_rig': (200, 505),
    'card_0': (121, 604), 'card_1': (191, 604), 'card_2': (261, 604), 'card_3': (331, 604),
    'water_sta': (104,640), 'water_end': (124, 660),
    'bridge_lef': (89, 280), 'bridge_rig': (289, 280),
    'opp_lit_lef': (89, 150), 'opp_lit_rig': (289, 150),
    'opp_bld_lef_sta': (75, 102), 'opp_bld_lef_end': (114, 103),
    'opp_bld_rig_sta': (275, 102), 'opp_bld_rig_end': (314, 103),
    'fight':(125,440),'sure':(190,600),'emtentrance': (35,563),
	'card_0_sta':(88,575),'card_0_end':(146,617),
	'card_1_sta':(160,575),'card_1_end':(218,617),
	'card_2_sta':(232,575),'card_2_end':(290,617),
	'card_3_sta':(304,575),'card_3_end':(362,617),
    'field_sta':(28,65),'field_end':(350,500),
    'emote0': (97,452), 'emote1': (165,452), 'emote2': (232,451), 'emote3': (298,451),
    'emote4': (97,513), 'emote5': (165,513), 'emote6': (232,513), 'emote7': (298,513),
    'whole_sta':(0,0),'whole_end':(381,677)
}


def get_ori():
    global orix,oriy
    sight=shtr.shot("cur_screen.png")
    orix,oriy=mtr.match_pos(sight,mtr.get_arr("Sources/core.png"))
    orix+=to_ori[0]
    oriy+=to_ori[1]
    print("Ori Token: ("+str(orix)+","+str(oriy)+")")

def display_bypos(card,desx,desy):
    tp.click(orix+poslib[card][0],oriy+poslib[card][1])
    time.sleep(0.3)
    if desx<poslib['field_sta'][0]:
        desx=poslib['field_sta'][0]
    if desy<poslib['field_sta'][1]:
        desy=poslib['field_sta'][1]
    if desx>poslib['field_end'][0]:
        desx=poslib['field_end'][0]
    if desy>poslib['field_end'][1]:
        desy=poslib['field_end'][1]
    tp.click(orix+desx,oriy+desy)

def display_byname(card,name):
    tp.click(orix+poslib[card][0],oriy+poslib[card][1])
    time.sleep(0.3)
    tp.click(orix+poslib[name][0],oriy+poslib[name][1])

def get_vector():
    curx,cury=tp.get_pos()
    return curx-orix,cury-oriy

def get_image(which,flg=""):
    # shot(which+flg+".png",orix+poslib[which+'_sta'][0],oriy+poslib[which+'_sta'][1],orix+poslib[which+'_end'][0],oriy+poslib[which+'_end'][1])
    return shtr.shot(orix+poslib[which+'_sta'][0],oriy+poslib[which+'_sta'][1],orix+poslib[which+'_end'][0],oriy+poslib[which+'_end'][1])

def next_fight():
    tp.click(orix+poslib['sure'][0],oriy+poslib['sure'][1])
    time.sleep(3)
    tp.click(orix+poslib['fight'][0],oriy+poslib['fight'][1])
    time.sleep(10)

def emoji(id):
    tp.click(orix+poslib['emtentrance'][0],oriy+poslib['emtentrance'][1])
    time.sleep(0.3)
    tp.click(orix+poslib['emote'+str(id)][0],oriy+poslib['emote'+str(id)][1])


if __name__=='__main__':
    print("Surgeon Here")
