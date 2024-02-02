import numpy as np
import cv2 as cv

distancesize = 6

def read(path):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    #img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)


    circle = findeCircle(img)
    angel = getAngle(cimg,circle)
    print(angel)
    rotated = rotate_image(cimg,angel)
    croped = crop(rotated,circle)
    Binary = decode(croped)
    Binary = Binary[13:len(Binary)]
    return Binary





def findeCircle(img):
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                                param1=10,
                                param2=40,
                                minRadius=1,
                                maxRadius=2000)
    circles = np.uint16(np.around(circles))
    circles = sorted(circles, key=lambda x: x[2], reverse=True)
    return circles[0][0]


def getAngle(img,c):
    n = 720
    step = 360 / n
    for u in range(n):
        t = np.radians(u * step)
        for r in range(int(c[2] * 0.97),int(c[2] * 1.05),4):
            y = int(r * np.sin(t) + c[1])
            x = int(r * np.cos(t) + c[0])
            if getcolor(img[x,y]):
                img[x,y] = [0,255,0]
                break
            else:
                img[x,y] = [255,0,0]
        else:
            cv.imwrite('Angel.png',img)
            return 180 - u * step + 1



def crop(cimg,c):
    x = c[0] - c[2]
    y = c[1] - c[2]
    h = c[2] * 2
    cv.imwrite('cimg.png',cimg)
    crop = cimg[y : y + h, x : x + h]
    return crop




def getheader(crop):
    x = int(len(crop) / 2)
    y = int(len(crop[0]) / 2)
    r = getRadius(crop)
    row = getRow(crop,x,y,r * 1.1,13)
    row.reverse()
    row.pop()
    return int(''.join(row),2)    

def getRadius(crop):
    x = int(len(crop) / 2)
    y = int(len(crop[0]) / 2)
    for i in range(y):
        if getcolor(crop[y + i,x]):
            return i


def calcCircles(e):
    sum = 0
    for i in range(1,e):
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        sum += n
        if(sum > e):
            return i + 1






def decode(crop):

    header = getheader(crop)
    radius = getRadius(crop)
    circles = calcCircles(header * 8)
    canvassize = circles * 30
    c = int(canvassize / 2)

    resized = cv.resize(crop, (canvassize, canvassize))
    resized[c,c] = [255,255,0]
    count = 0
    Binary = []
    for i in range(1,circles):
        r = c / circles * i + 1
        n = int(100 / 8 * i * np.pi * 2 / distancesize)
        Binary += getRow(resized,c,c,r,n)
    cv.imwrite('resized.png', resized)
    return Binary




def getRow(img,ix,iy,r,n):
    Binary = []
    step = 360 / n
    for u in range(n):
        t = np.radians(u * step)
        y = int(r * np.sin(t) + ix)
        x = int(r * np.cos(t) + iy)
        if getcolor(img[x,y]):
            img[x,y] = [0,255,0]
            #cv.circle(img,(y,x),int(x / 100),(0,255,0),-1)
            Binary.append("1")
        else:
            img[x,y] = [255,0,0]
            #cv.circle(img,(y,x),int(y / 100),(255,0,0),-1)
            Binary.append("0")
        #cv.putText(img,str(len(Binary)),(x,y),1,1,(0,0,255),1)
    #debug(img)
    return Binary

def debug(canva):
    cv.imshow('resized',canva)
    cv.waitKey(0)
    # if cv.waitKey(1) == ord('q'): 
    #     return 1

def getAverage(list):
    return int(sum(list) / len(list))

def getcolor(p):
    return getAverage(p) <= 125

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
  return result



if __name__ == '__main__':
    from Encrypt import *
    code = read('output.png')
    print(BinaryToText(code))
