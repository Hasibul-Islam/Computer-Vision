import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blanck',blank)

# Paint the image a certain color

# blank[200:300,300:400]=0,255,0
# cv.imshow('Green',blank)

cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=-1) #imageName, origin, height, widht, color, thickness
cv.imshow('Rectangle',blank)

cv.circle(blank,(250,250),40,(0,0,255),thickness=30) # imageName, centerPosition, Radius, Color, Thickness
cv.imshow('Circle',blank)
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=30) #imageName,origin,endPoint, Color
cv.imshow('Line',blank)

cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=3)

cv.imshow('Text',blank)
cv.waitKey(5000)
