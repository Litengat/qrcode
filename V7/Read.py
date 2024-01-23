import numpy as np
import cv2 as cv

distancesize = 6

def read(path):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    #img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                                param1=10,
                                param2=40,
                                minRadius=1,
                                maxRadius=2000)
    circles = np.uint16(np.around(circles))
    circles = sorted(circles, key=lambda x: x[2], reverse=True)
    circle = circles[0][0]
    crops = crop(cimg,circle)
    Binary = decode(crops)
    return Binary

def crop(cimg,c):
    print(c)
    x = c[0] - c[2]
    y = c[1] - c[2]
    h = c[2] * 2
    for i in range(x,x + h):
        cimg[i,y] = [255,0,0]
    for v in range(y,y + h):
        cimg[x,v] = [255,0,0]
    cv.imwrite('cimg.png',cimg)
    crop = cimg[y : y + h, x : x + h]
    return crop
def getheader(cimg,x,y):
    for i in range(y,0):
        print(getRow(cimg,x,y))

def calcCircles(e):
    sum = 0
    for i in range(2,e):
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        sum += n
        if(sum > e):
            return i 






def decode(crop):
    circles = 10
    canvassize = circles * 30
    c = int(canvassize / 2)

    resized = cv.resize(crop, (canvassize, canvassize))
    resized[c,c] = [255,255,0]
    count = 0
    Binary = []
    for i in range(1,circles):
        r = c / circles * i 
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        Binary += getRow(resized,c,c,r,n)
            #cv.putText(resized,str(count),(x,y),1,1,(0,0,255),1)
    cv.imwrite('resized.png', resized)
    return Binary

def getRow(img,x,y,r,n):
    Binary = []
    step = 360 / n
    for u in range(n):
        t = np.radians(u * step)
        x = int(r * np.sin(t) + x)
        y = int(r * np.cos(t) + y)
        if getcolor(img[x,y]):
            img[x,y] = [0,255,0]
            #cv.circle(resized,(y,x),int(canvassize / 200),(0,255,0),-1)
            Binary.append("1")
        else:
            img[x,y] = [255,0,0]
            #cv.circle(resized,(y,x),int(canvassize / 200),(255,0,0),-1)
            Binary.append("0")
        #debug(img)
    return Binary

def debug(canva):
    cv.imshow('resized',canva)
    if cv.waitKey(1) == ord('q'): 
        return 1

def getAverage(list):
    return int(sum(list) / len(list))

def getcolor(p):
    return getAverage(p) > 125

if __name__ == '__main__':
    from Encrypt import *
    code = read('output.png')
    print(BinaryToText(code))
