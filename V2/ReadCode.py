import cv2
import numpy as np
from Encrypt import *

def ReadFromImage():
    img = cv2.imread('IMG/crop.png',0)
    rows,cols = img.shape

    result = ""

    for i in range(rows):
        for j in range(cols):
            k = img[i,j]
            if k > 125:
                result += "1"
            if k <= 125:
                result += "0"


    
    length = int(BinaryToText(result[:16]))


    return result[16:((length*8+16))]

def CropFromPhoto():
    image = cv2.imread('IMG/Code.png')
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (25,25), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Perform morph operations, first open to remove noise, then close to combine
    noise_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, noise_kernel, iterations=2)
    close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, close_kernel, iterations=3)

    # Find enclosing boundingbox and crop ROI
    coords = cv2.findNonZero(close)
    x,y,w,h = cv2.boundingRect(coords)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    crop = original[y:y+h, x:x+w]

    resized = cv2.resize(crop,(20, 40))
    cv2.imwrite('IMG/crop.png', resized)
    # cv2.imshow('crop', resized)
    cv2.waitKey()