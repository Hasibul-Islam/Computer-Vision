import cv2 as cv
def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)

img = cv.imread('Photos/war_horse.png')

# cv.imshow('Screenshot',img)
#GrayScale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray screen',gray)
#Blur
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
#Edges
canny = cv.Canny(gray,125,175)
cv.imshow('War Horse',rescaleFrame(canny))
#Dilated Edges
dilated = cv.dilate(rescaleFrame(canny),(7,7),iterations=3)
cv.imshow('Dilated', dilated)

#eroded

eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#resize

resized =cv.resize(eroded,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#cropping

cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)