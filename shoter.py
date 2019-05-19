from PIL import ImageGrab

def shot(name,x1=None,y1=None,x2=None,y2=None):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        ImageGrab.grab().save(name)
    else:
        ImageGrab.grab((x1,y1,x2,y2)).save(name)

if __name__=='__main__':
    print("Shoter Here")
