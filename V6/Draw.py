import numpy as np
import cv2 as cv
import time 
size = 5
canvassize = 1000
c = int(canvassize / 2)

def gernerate(Binary,path):
    canva = np.ones((canvassize,canvassize,1))
    canva.fill(255)
    count = 0
    for i in range(1,8):
        r =  canvassize / 16 * i 
        n = int(100 / 8 * i * np.pi * 2 / size)
        step = 360 / n
        #cv.circle(canva,(c,c),int(r),(100,100,100),int(canvassize / 500))
        for u in range(n):
            t = np.radians(u * step)
            x = int(r * np.sin(t) + c)
            y = int(r * np.cos(t) + c)
            if len(Binary) > count:
                if Binary[count] == '1':
                    cv.circle(canva,(y,x),int(canvassize / 100),(0,0,0),-1)
            else:
                break
            #debug(canva)
            count += 1
    cv.circle(canva,(c,c),int(c * 0.989),(0,0,0),int(canvassize / 100))
    cv.imwrite(path,canva)


def debug(canva):
    cv.imshow('resized',canva)
    if cv.waitKey(1) == ord('q'): 
        return 0
    time.sleep(0.1)
    return 1





if __name__ == '__main__':
    from Encrypt import *
    gernerate(TextToBinary("max"),"output.png")