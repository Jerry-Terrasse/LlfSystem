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
    'archer':{'id':0,'cost':3,'pos':(0,80),'type':'troop'},
    'arrows':{'id':1,'cost':3,'pos':(0,10),'type':'spell'},
    'babydrgn':{'id':2,'cost':4,'pos':(0,50),'type':'troop'},
    'battleram':{'id':9,'cost':4,'pos':'bridge_','type':'thief'},
    'bomber':{'id':11,'cost':3,'pos':(0,80),'type':'troop'},
    'cannon':{'id':13,'cost':3,'pos':'center_','type':'building'},
    'gobbarrel':{'id':30,'cost':3,'pos':'opp_lit_','type':'thief'},
    'knight':{'id':47,'cost':3,'pos':(0,10),'type':'troop'},
    'minion':{'id':56,'cost':3,'pos':(0,40),'type':'troop'},
    'minipeeka':{'id':57,'cost':4,'pos':(0,40),'type':'troop'},
    'prince':{'id':64,'cost':5,'pos':(0,20),'type':'troop'},
    'skegiant':{'id':76,'cost':6,'pos':(0,0),'type':'troop'},
    'valkyrie':{'id':85,'cost':4,'pos':(0,10),'type':'troop'},
    'wallbrkr':{'id':86,'cost':3,'pos':'bridge_','type':'thief'},
    'witch':{'id':87,'cost':5,'pos':(0,70),'type':'troop'},
    'skearmy':{'id':74,'cost':3,'pos':(0,0),'type':'troop'},
    'UNKNOWN':{'id':-1,'cost':99,'pos':(0,0),'type':''}
}


def meeting():
    global posx,posy,fire,bld_lef,bld_rig,water,cards
    wait=False
    cards=dcd.get_card()
    bld_lef=dcd.get_bld("opp_bld_lef")
    bld_rig=dcd.get_bld("opp_bld_rig")
    if bld_lef<bld_rig:
        posext='lef'
    else:
        posext='rig'
    posx,posy,fire=dcd.war_at()
    water=dcd.get_water()
    echo()
    if fire>=100:
        for card in cards:
            if fire<=1000 and cardlib[card]['type']=='thief' and water>=cardlib[card]['cost']+3:
                posname=cardlib[card]['pos']+posext
                water-=cardlib[card]['cost']
                sgn.display_byname('card_'+str(cards.index(card)),posname)
                wait=card=='gobbarrel'
                continue
            if cardlib[card]['type']=='troop' and cardlib[card]['cost']<=water:
                sgn.display_bypos('card_'+str(cards.index(card)),posx+cardlib[card]['pos'][0],posy+cardlib[card]['pos'][1])
                return wait
    else:
        if water>=8:
            minc=11
            id=0
            for card in cards:
                if cardlib[card]['type']=='thief' or cardlib[card]['type']=='building':
                    if minc>cardlib[card]['cost']:
                        minc=cardlib[card]['cost']
                        id=card
            if id!=0:
                posname=cardlib[id]['pos']+posext
                sgn.display_byname('card_'+str(cards.index(id)),posname)
                wait=id=='gobbarrel'
            for card in cards:
                if True: # for spell
                    if minc>cardlib[card]['cost']:
                        minc=cardlib[card]['cost']
                        id=card
            sgn.display_byname('card_'+str(cards.index(id)),'bottom_'+posext)
    return wait

def echo():
    print(water, cards, "(%d, %d)" % (bld_lef,bld_rig), "{%d,%d,%d}" % (posx,posy,fire))


if __name__=='__main__':
    print("Policians Here")