import cv2 as cv

img = cv.imread('Photos/group.png')  
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Image Gray', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

faces_rect = haar_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found: {len(faces_rect)} \nCo-ordinates (for all faces): {faces_rect}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=2)

cv.imshow('Faces Detected', img)

cv.waitKey(0)