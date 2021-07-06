
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/casual_me_close.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian Edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lablacian', lap)

# Sobel

Sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)

Sobely = cv.Sobel(gray, cv.CV_64F, 0,1)

combined_sobel = cv.bitwise_or(Sobely,Sobelx)

cv.imshow('Sobelx', Sobelx)
cv.imshow('Sobely', Sobely)

cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)

cv.imshow('Canny', canny)
cv.waitKey(0)