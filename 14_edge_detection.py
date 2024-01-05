import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# ---------- Laplacian ----------
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian (Edge Detector)', lap)

# ---------- Canny ----------
canny = cv.Canny(gray, threshold1=150, threshold2=175)
cv.imshow('Canny (Edge Detector)', canny)
 

# ---------- Sobel ----------
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)
# We want to superimpose sobelX and sobelY
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined SobelX & SobelY', combined_sobel)

cv.waitKey(0)