from matcher import *
from surgeon import *
from regulator import *

same_cnt=int()
pre_water=int()

ignore_rec=[(0,0,380,37),(161,37,217,105),(72,105,107,135),(271,105,306,135),(72,376,107,411),(161,411,217,470),(271,376,306,411),(0,511,380,676)]

'''
ignore_rec={
    'opp_big_sta':(),'opp_big_end':(),
    'opp_lit_lef_sta':(),'opp_lit_lef_end':(),
    'opp_lit_rig_sta':(),'opp_lit_rig_end':(),
    'slf_big_sta':(),'slf_big_end':(),
    'slf_lit_lef_sta':(),'slf_lit_lef_end':(),
    'slf_lit_rig_sta':(),'slf_lit_rig_end':()
}
'''

def get_water():
    global pre_water,same_cnt
    maxv=int()
    val=int()
    ans=int()
    get_image("water")
    for i in range(11):
        val=simularity("water.png","Sources/water_"+str(i)+".png")
        if(maxv<val):
            maxv=val
            ans=i
    if ans==pre_water:
        same_cnt+=1
        if same_cnt>3:
            same_cnt=0
            fight_end()
            return -1
    else:
        same_cnt=0
        pre_water=ans
    return ans

def get_bld(which):
    ret=int()
    get_image(which)
    bld=get_arr(which+".png",2)
    bld=get_two(bld,144)
    line,col=bld.shape
    for i in range(col):
        if bld[0][i]==0:
            break
        ret=i
    return ret

def war_at():
    get_image("whole","0")
    get_image("whole","1")
    retx=int()
    rety=int()
    cnt=int()
    map=match_diff("whole0.png","whole1.png")
    x,y,z=map.shape
    for rec in ignore_rec:
        map[rec[1]:rec[3],rec[0]:rec[2],:] = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if map[i][j][k]:
                    retx+=j # x,y=y,x
                    rety+=i
                    cnt+=1
    if cnt:
        return retx//cnt,rety//cnt
    else:
        return 0,0

if __name__=='__main__':
    print("Decoder Here")
