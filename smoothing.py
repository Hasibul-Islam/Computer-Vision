import cv2 as cv
import numpy as np

img = cv.imread('Photos/casual_me_close.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# average blur

average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# gaussian blur

guass = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Gaussian Blur', guass)

# median blur

median = cv.medianBlur(img, 7)

cv.imshow('Median Blur', median)

# bilateral blur

bilate = cv.bilateralFilter(img, 5, 35, 25) #image, diameter, sigmacolor--> more color from 
# other closer pixels,  , 

cv.imshow('Bilateral', bilate)

cv.waitKey(0)