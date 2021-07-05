import cv2 as cv
import numpy as np
img = cv.imread('Photos/casual_me_close.jpg')

blank = np.zeros((img.shape[:2]),dtype='uint8')
# cv.imshow('Blanck',blank)
# cv.imshow('Screenshot',img)
#GrayScale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray screen',gray)
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
# resized =cv.resize(thresh,(250,250),interpolation=cv.INTER_AREA)
# cv.imshow('Resized',resized)
cv.imshow('Thresh', thresh)
#Blur
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

canny = cv.Canny(gray,125,175)

# mathematical edges

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(55,50,255),1)
cv.imshow('Contours Drawn', blank)
resized =cv.resize(blank,(250,250),interpolation=cv.INTER_AREA)
cv.imshow('Contours',resized)
cv.waitKey(0)