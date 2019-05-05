import time

ori_time=int()
cur_time=int()
started=False
double_water=False

def fight_start():
  global ori_time,started,double_water
  ori_time=time.time()
  started=True
  double_water=False

def fight_end():
  global started,double_water
  started=False
  double_water=True

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

if __name__=='__main__':
  print("Regulator Here")