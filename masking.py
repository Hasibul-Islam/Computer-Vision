import cv2 as cv
import numpy as np

img = cv.imread('Photos/casual_me_close.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('Masked Image', masked)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(), (200,200),200,255,-1)

weird_shape = cv.bitwise_and(rectangle,circle)

masked = cv.bitwise_and(img,img, mask=weird_shape)
cv.imshow('Weired Shaped Masked Image', masked)
cv.waitKey(0)