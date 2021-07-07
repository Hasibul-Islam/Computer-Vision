import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/casual_me_close.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_casecade = cv.CascadeClassifier('haar_face.xml')
# faces_rect = haar_casecade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=7)
# print(len(faces_rect))
# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=3)
    

# cv.imshow('Detected Face',img)

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)


capture = cv.VideoCapture('Videos/Video 3 Sci-Fi Movie Review.mp4')


while True:
    isTrue, frame = capture.read()
    
    resizedFrame = rescaleFrame(frame)
    gray = cv.cvtColor(resizedFrame,cv.COLOR_BGR2GRAY)
    faces_rect = haar_casecade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    print(len(faces_rect))
    for (x,y,w,h) in faces_rect:
        cv.rectangle(resizedFrame, (x,y), (x+w, y+h), (0,255,0), thickness=3)
    # cv.imshow('Video Org',frame)
    cv.imshow('Video resized',resizedFrame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
