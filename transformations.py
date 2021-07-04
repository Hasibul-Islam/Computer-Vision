import cv2 as cv
import numpy as np

img = cv.imread('Photos/war_horse.png')

# cv.imshow('Original',img)
# shift image
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,x]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


# -x => left
# -y => up
# x => right
# y => down

# rotate image
def roatate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0) # rotate point, angle, scale
    dimnesions = (width,height)
    return cv.warpAffine(img, rotMat, dimnesions)


roatated = roatate(img,45)
# cv.imshow('Rotated',roatated)


translated = translate(img,100,100)
# cv.imshow('Translated', translated)

#filliping

flip = cv.flip(img, 0)
cv.imshow('Flipped',flip)


cv.waitKey(0)