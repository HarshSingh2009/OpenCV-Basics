import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')
cv.imshow('BGR', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

# Splitting into different color channels - Blue, Green, Red

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue Gray', b)
cv.imshow('Green Gray', g)
cv.imshow('Red Gray', r)

cv.imshow('Blue Blue', blue)
cv.imshow('Green Green', green)
cv.imshow('Red red', red)

print(f'Image Shape: {img.shape} \nRed channel: {r.shape} \nGreen channel: {g.shape} \nBlue Channel: {b.shape}')

# Merging all color channels to form colorized image
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

print(f'Merged Image Shape: {merged.shape}')


cv.waitKey(0)