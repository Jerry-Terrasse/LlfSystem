from PIL import ImageGrab as ig
import numpy as np


def shot(x1=None,y1=None,x2=None,y2=None,name=None):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        ret=ig.grab()
    else:
        ret=ig.grab((x1,y1,x2,y2))
    if name is not None:
        ret.save(name)
    return np.array(ret)[:,:,::-1]


if __name__=='__main__':
    print("Shoter Here")
