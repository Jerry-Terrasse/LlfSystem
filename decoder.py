from matcher import *
from surgeon import *
from regulator import *
import time
import cv2 as cv


same_cnt=int()
pre_water=int()

ignore_rec=[(0,0,380,37),(161,37,217,105),(72,105,107,135),(271,105,306,135),(72,376,107,411),(161,411,217,470),(271,376,306,411),(0,511,380,676),(217,443,350,511)]

deck = ("cannon","battleram","prince","witch","skegiant","skearmy","gobbarrel","valkyrie")

waters=list()
icons=list()


def get_card():
    ans = ["", "", "", ""]
    crd = [get_image("card_"+str(i)) for i in range(4)]
    for i in range(4):
        maxv = 0
        for j in range(8):
            val = similarity(icons[j], crd[i])
            if maxv < val:
                maxv = val
                ans[i] = deck[j]
        if maxv < 420000:
            ans[i] = "UNKNOWN"
    #print(ans)
    return ans

def get_water():
    global pre_water,same_cnt
    maxv=int()
    val=int()
    ans=int()
    wtr=get_image("water")
    for i in range(11):
        # val=similarity("water.png","Sources/water_"+str(i)+".png")
        val=similarity(wtr,waters[i])
        if maxv<val:
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
    bld=get_image(which)
    # bld=get_arr(which+".png")
    for i in bld[0]:
        ret+=i[0]<100 or i[0]>200
        ret+=i[1]<100 or i[1]>200
    if ret<20:
        return 99
    ret=0
    bld=bld[:,:,2]
    bld=get_two(bld,144)
    line,col=bld.shape
    for i in range(col):
        if bld[0][i]==0:
            break
        ret=i
    return ret

def war_at():
    sight=get_image("whole")
    sight_=get_image("whole")
    #cv.imwrite("D:/"+str(time.time())+".png",sight);
    #cv.imwrite("D:/"+str(time.time())+".png",sight_);
    retx=int()
    rety=int()
    cnt=int()
    map=match_diff(sight,sight_)
    x,y,z=map.shape
    for rec in ignore_rec:
        map[rec[1]:rec[3],rec[0]:rec[2],:] = 0
    for i in range(280,x):
        for j in range(y):
            for k in range(z):
                if map[i][j][k]:
                    retx+=j # x,y=y,x
                    rety+=i
                    cnt+=1
    if cnt:
        # print("DECODER: war at (%d,%d,%d)" % (retx//cnt,rety//cnt,cnt))
        # print("war{%d,%d,%d}" % (retx//cnt,rety//cnt,cnt))
        return retx//cnt,rety//cnt,cnt
    else:
        #print("war{}")
        return 0,0,0

def load_images():
    global waters,icons
    waters=[get_arr("Sources/water_"+str(i)+".png") for i in range(11)]
    icons=[get_arr("Sources/cardlib/"+i+".png") for i in deck]
    return

if __name__=='__main__':
    print("Decoder Here")
