import numpy as np
import cv2 as cv
import drawsvg as draw

size = 5
    
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
    cv.circle(cimg,(circle[0],circle[1]),1,(255,0,0),3)
    cv.circle(cimg,(circle[0],circle[1]),circle[2],(255,0,0),3)
    Binary = []
    counter = 0
    for i in range(1,8):
        r = circle[2] / 8 * i 
        n = int(100 / 8 * i * np.pi * 2 / size)
        step = 360 / n
        for u in range(n):
            t = np.radians(u * step) - 11
            x = int(r * np.cos(t) + circle[1])
            y = int(r * np.sin(t) + circle[0])
            cimg[x,y] = [255,0,0]  

    cv.imshow('detected circles',cimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return Binary


    

def getAverage(list):
    return int(sum(list) / len(list))

    

if __name__ == '__main__':
    print(read('V5/test.png'))
            








  
    
#cv.circle(cimg,(x,y),1,(int(color[0]),int(color[1]),int(color[2])),3)
# average = []
# for i in range(-2,2):
#     for z in range(-2,2):
#         average.append(getAverage(cimg[x + i,y + z]))
# print(average)
# color = getAverage(average)
# print(color)

# if color > 125:
#     cv.circle(cimg,(x,y),1,(255,0,0),3)
#     return "1"
# if color <= 125:
#     cv.circle(cimg,(x,y),1,(0,255,0),3)
#     return "0"
