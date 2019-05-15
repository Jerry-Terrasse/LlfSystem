import os
import time

# (80) (220,835) (360) (500)
# (290,666)



def adb_click(x,y):
    os.system("adb_server shell input tap "+str(x)+" "+str(y))


if __name__=='__main__':
    print("Opener Here")
    time.sleep(3600*3)
    adb_click(220,835)
    time.sleep(20)
    adb_click(290,666)
    time.sleep(3600*3)
    adb_click(500,835)
    time.sleep(20)
    adb_click(290,666)
    time.sleep(3600*3)
    adb_click(80,835)
    time.sleep(20)
    adb_click(290,666)
    os.system("notepad")
