from matcher import *
from surgeon import *

def get_water():
  maxv=int()
  val=int()
  ans=int()
  get_water_image()
  for i in range(11):
    val=simularity("cur_water.png","Sources/water_"+str(i)+".png")
    if(maxv<val):
      maxv=val
      ans=i
  return ans
    

if __name__=='__main__':
  print("Decoder Here")
