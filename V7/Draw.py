import numpy as np
import cv2 as cv
import time 

distancesize = 6

def gernerate(Binary,path):

    
    print(calcCircles(len(Binary)))
    length = len(Binary)
    Binary = length + Binary
    print(Binary)


    circles = calcCircles(len(Binary))
    canvassize = circles * 110
    dotsize = int(circles * 100 / (15 * circles))
    c = int(canvassize / 2)
    radius = int(c * 0.9)

    canvas = np.ones((canvassize,canvassize,1))
    canvas.fill(255)
    count = 0
    cv.ellipse(canvas,(c,c),(radius,radius),0,270,-80,(0,0,0),dotsize)
    for i in range(1,circles):
        r = radius / circles * i
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        step = 360 / n
        #cv.circle(canva,(c,c),int(r),(100,100,100),int(canvassize / 500))
        for u in range(n):
            t = np.radians(u * step)
            x = int(r * np.sin(t) + c)
            y = int(r * np.cos(t) + c)
            if len(Binary) > count:
                if Binary[count] == '1':
                    cv.circle(canvas,(y,x),dotsize,(0,0,0),-1)
            else:
                 break
            debug(canvas)
            count += 1
    cv.imwrite(path,canvas)


def tobin(x,s):
    return [(x>>k)&1 for k in range(0,s)]


def debug(canvas):
    cv.imshow('resized',canvas)
    if cv.waitKey(1) == ord('q'): 
        return

def calcCircles(e):
    sum = 0
    for i in range(1,e):
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        sum += n
        if(sum > e):
            return i 




if __name__ == '__main__':
    from Encrypt import *
    gernerate(TextToBinary("Maximilian"),'output.png')