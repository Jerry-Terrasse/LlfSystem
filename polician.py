import surgeon as sgn
import decoder as dcd

cardlib={
    'archer':{'id':0,'cost':3,'pos':(0,80)},
    'babydrgn':{'id':2,'cost':4,'pos':(0,50)},
    'bomber':{'id':11,'cost':3,'pos':(0,80)},
    'wallbrkr':{'id':86,'cost':3,'pos':(0,-10)},
    'knight':{'id':47,'cost':3,'pos':(0,10)},
    'minion':{'id':56,'cost':3,'pos':(0,40)},
    'minipeeka':{'id':57,'cost':4,'pos':(0,40)},
    'valkyrie':{'id':85,'cost':4,'pos':(0,10)},
    'UNKNOWN':{'id':-1,'cost':99,'pos':(0,0)}
}

def meeting(water,bld_lef,bld_rig,cards):
    posx,posy,fire=dcd.war_at()
    if fire>=100:
        for i in range(4):
            if cards[i]!='wallbrkr' and cardlib[cards[i]]['cost']<=water:
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
                if cards[i]=='wallbrkr':
                    sgn.display_byname('card_'+str(i),'bridge_'+posname)
                    return
                if cardlib[cards[i]]['cost']<minc:
                    minc=cardlib[cards[i]]['cost']
                    id=i
            sgn.display_byname('card_'+str(i),'bottom_'+posname)
    return

if __name__=='__main__':
    print("Policians Here")