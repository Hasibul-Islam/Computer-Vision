import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/casual_me_close.jpg')

# simple thresholding

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)

cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)

# cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold', adaptive_threshold)


cv.waitKey(0)