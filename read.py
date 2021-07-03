import cv2 as cv
# Reading Images
# img = cv.imread('Photos/war_horse.png')

# cv.imshow('Screenshot',img)

# Change Resolution # will work for live video

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)



#Rescaling Video # will work for existing video or photos



def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)

#Reading Video

capture = cv.VideoCapture('Videos/Video 1 Shakib.mp4')


while True:
    isTrue, frame = capture.read()
    
    resizedFrame = rescaleFrame(frame)
    cv.imshow('Video Org',frame)
    cv.imshow('Video resized',resizedFrame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(5000)