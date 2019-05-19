from matcher import *
from surgeon import *
from regulator import *

same_cnt=int()
pre_water=int()

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
    retx=int()
    rety=int()
    cnt=int()
    get_image("whole","1")
    map=match_diff("whole0.png","whole1.png")
    x,y,z=map.shape
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
        fight_end()
        return 0,0

if __name__=='__main__':
    print("Decoder Here")
