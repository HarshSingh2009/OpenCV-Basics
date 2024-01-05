import cv2 as cv
import numpy as np


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# Creating a mask
mask = cv.circle(img=blank, center=(img.shape[1]//2, img.shape[0]//2), radius=100, color=255, thickness=-1)
cv.imshow('Mask', mask)

# Using Mask
masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_image)

cv.waitKey(0)