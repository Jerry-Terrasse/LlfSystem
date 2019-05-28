import time
from surgeon import *


ori_time=int()
cur_time=int()
pre_time=int()
waves=int()
double_water=False
AUTO=False


def fight_start():
    global ori_time,started,double_water,pre_time
    ori_time=time.time()
    pre_time=0
    started=True
    double_water=False

def fight_end():
    global started
    print("Fight Finished.")
    if AUTO:
        next_fight()
        fight_start()
    else:
        exit()

def time_past():
    global cur_time
    cur_time=time.time()
    return int(cur_time-ori_time)

def wait():
    global double_water,cur_time
    if double_water:
        time.sleep(3)
    else:
        cur_time=time.time()
        if cur_time-ori_time>=120:
            double_water=True
            time.sleep(3)
        else:
            time.sleep(5)

def Fight():
    global waves,cur_time,pre_time
    cur_time=time.time()
    if cur_time-pre_time>=30:
        waves+=1
        # pre_time=cur_time
        return True
    else:
        return False

def set_pre_time():
    global pre_time
    pre_time=time.time()


if __name__=='__main__':
    print("Regulator Here")