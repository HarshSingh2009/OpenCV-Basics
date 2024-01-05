import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(img=blank.copy(), pt1=(30, 30), pt2=(370, 370), color=255, thickness=-1)
circle = cv.circle(blank.copy(), center=(200, 200), radius=200, color=255, thickness=-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> Inverse colors - 1 to 0 and vice versa
rectangle_bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT', rectangle_bitwise_not)

circle_bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', circle_bitwise_not)


cv.waitKey(0)