import surgeon as sgn
import decoder as dcd
from random import randint

posx=int()
posy=int()
fire=int()
water=int()
bld_lef=int()
bld_rig=int()
cards=list()

cardlib={
    'archer':{'id':0,'cost':3,'pos':(0,80)},
    'arrows':{'id':1,'cost':3,'pos':(0,10)},
    'babydrgn':{'id':2,'cost':4,'pos':(0,50)},
    'bomber':{'id':11,'cost':3,'pos':(0,80)},
    'gobbarrel':{'id':30,'cost':3,'pos':(0,0)},
    'knight':{'id':47,'cost':3,'pos':(0,10)},
    'minion':{'id':56,'cost':3,'pos':(0,40)},
    'minipeeka':{'id':57,'cost':4,'pos':(0,40)},
    'skegiant':{'id':76,'cost':6,'pos':(0,0)},
    'valkyrie':{'id':85,'cost':4,'pos':(0,10)},
    'wallbrkr':{'id':86,'cost':3,'pos':(0,-10)},
    'witch':{'id':87,'cost':5,'pos':(0,70)},
	'skearmy':{'id':74,'cost':3,'pos':(0,0)},
    'battleram':{'id':9,'cost':4,'pos':(0,-10)},
    'UNKNOWN':{'id':-1,'cost':99,'pos':(0,0)}
}


def meeting():
    global posx,posy,fire,bld_lef,bld_rig,water,cards
    cards=dcd.get_card()
    bld_lef=dcd.get_bld("opp_bld_lef")
    bld_rig=dcd.get_bld("opp_bld_rig")
    posx,posy,fire=dcd.war_at()
    water=dcd.get_water()
    echo()
    if fire>=100:
        for i in range(4):
            if water>=5 and fire<=1000 and cards[i]=='gobbarrel':
                if bld_lef<bld_rig:
                    posname='lef'
                else:
                    posname='rig'
                water-=3
                sgn.display_byname('card_'+str(i),'opp_lit_'+posname)
                continue
            if cards[i]!='gobbarrel' and cards[i]!='battleram' and cardlib[cards[i]]['cost']<=water:
                sgn.display_bypos('card_'+str(i),posx+cardlib[cards[i]]['pos'][0],posy+cardlib[cards[i]]['pos'][1])
                return
    else:
        if water>=8:
            if bld_lef<bld_rig:
                posname='lef'
            else:
                posname='rig'
            minc=10
            id=0
            for i in range(4):
                if cards[i]=='gobbarrel':
                    sgn.display_byname('card_'+str(i),'opp_lit_'+posname)
                    return
                if cards[i]=='battleram':
                    sgn.display_byname('card_'+str(i),'bridge_'+posname)
                    return
                if cardlib[cards[i]]['cost']<minc:
                    minc=cardlib[cards[i]]['cost']
                    id=i
            sgn.display_byname('card_'+str(i),'bottom_'+posname)
    return

def echo():
    print(water, cards, "(%d, %d)" % (bld_lef,bld_rig), "{%d,%d,%d}" % (posx,posy,fire))
    sgn.emoji(randint(0,5))


if __name__=='__main__':
    print("Policians Here")