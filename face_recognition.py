import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'E:\Self Task\Computer Vision\Practice One\Photos\Faces\val\md_hasibul_islam\2.jpg')

resized =cv.resize(img,(400,400),interpolation=cv.INTER_AREA)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(resized, str(people[label]), (50,200), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
    cv.rectangle(resized, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', resized)

cv.waitKey(0)