import numpy as np
import cv2 as cv
size = 5
cropsize = 1000
c = int(cropsize / 2)



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
    x = circle[0] - circle[2]
    y = circle[1] - circle[2]
    h = circle[2] * 2
    crop = cimg[y : y + h, x : x + h]
    resized = cv.resize(crop, (cropsize, cropsize))
    count = 0
    Binary = []
    for i in range(1,8):
        r =  cropsize / 15.7 * i 
        n = int(100 / 8 * i * np.pi * 2 / size)
        step = 360 / n
        for u in range(n):
            t = np.radians(u * step)
            x = int(r * np.sin(t) + c)
            y = int(r * np.cos(t) + c)
            color = getAverage(resized[x,y])
            if color > 125:
                cv.circle(resized,(y,x),int(cropsize / 200),(255,0,0),-1)
                Binary.append("0")
            if color <= 125:
                #resized[x,y] = [0,255,0]
                cv.circle(resized,(y,x),int(cropsize / 200),(0,255,0),-1)
                Binary.append("1")
            cv.putText(resized,str(Binary),(0,900),1,1,(0,0,255),1)
            debug(resized)
            count += 1
            #cv.putText(resized,str(count),(x,y),1,1,(0,0,255),1)
    cv.imwrite('resized.png', resized)
    return Binary


def debug(canva):
    cv.imshow('resized',canva)
    if cv.waitKey(1) == ord('q'): 
        return 1

def getAverage(list):
    return int(sum(list) / len(list))


if __name__ == '__main__':
    from Encrypt import *
    code = read('V6/test.png')
    print(code)
    print(BinaryToText(code))
