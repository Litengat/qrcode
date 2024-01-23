import numpy as np
import cv2 as cv
import math
import drawsvg as draw

size = 5
    
def read():
    img = cv.imread('V5/test.png', cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)


    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                                param1=10,
                                param2=40,
                                minRadius=1,
                                maxRadius=1000)
    circles = np.uint16(np.around(circles))
    circles = sorted(circles, key=lambda x: x[2], reverse=True)
    circle = circles[0][0]
    d = draw.Drawing(256, 256, origin='center')
    for i in range(1,8):
        r = int(100 / 8 * i * 1.025) 
        n = int(r * np.pi * 2 / size) 
        print(n)
        step = 360 / n
        d.append(draw.Circle(10, 10, r,fill='none',stroke='black', stroke_width=0.5))
        for u in range(n):
            t = np.radians(u * step)
            x = int(r * np.cos(t) + circle[1])
            y = int(r * np.sin(t) + circle[2])
            cv.circle(cimg,(x,y),2,(255,0,0),3)
    cv.imshow('detected circles',cimg)
    cv.waitKey(0)
    cv.destroyAllWindows()


read()
            
        

