import numpy as np
import cv2 as cv
import time 

distancesize = 6

def gernerate(Binary,path):

    


    length = int(len(Binary) / 8)
    Binary = ["1"] + tobin(length,12) + Binary
    circles = calcCircles(len(Binary))
    print("circles: " + str(circles))
    canvassize = circles * 110
    dotsize = int(circles * 100 / (15 * circles))
    c = int(canvassize / 2)
    radius = int(c * 0.9)




    canvas = np.ones((canvassize,canvassize,1))
    canvas.fill(255)
    count = 0


    cv.ellipse(canvas,(c,c),(radius,radius),0,265,-90,(0,0,0),dotsize * 2)
    for i in range(1,circles):
        r = radius / circles * i 
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        step = 360 / n
        #cv.circle(canva,(c,c),int(r),(100,100,100),int(canvassize / 500))
        Binary.insert(count,'1')
        for u in range(n):
            t = np.radians(u * step)
            x = int(r * np.sin(t) + c)
            y = int(r * np.cos(t) + c)
            if len(Binary) > count:
                if Binary[count] == '1':
                    cv.circle(canvas,(x,y),dotsize,(0,0,0),-1)
            else:
                break
            #print(count)
            count += 1
            #cv.putText(canvas,str(count),(x,y),1,1,(0,0,255),1)
            #debug(canvas)
    #canvas = rotate_image(canvas,120)
    cv.imwrite(path,canvas)


def tobin(x,s):
    return [str((x>>k) & 1) for k in range(0,s)]


def debug(canvas):
    cv.imshow('resized',canvas)
    if cv.waitKey(1) == ord('q'): 
        return

def calcCircles(e):
    sum = 0
    for i in range(1,e):
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        sum += n - 1
        if(sum > e):
            return i + 1

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
  return result



if __name__ == '__main__':
    from Encrypt import *
    from Read import read
    gernerate(TextToBinary("Maximilian Mennicken"),'output.png')
    code = read('output.png')
    print(BinaryToText(code))
