import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray-scaled', gray_img)

"""
One way of finding Contours is to first blur the image, then find edges, and then count the contours
"""

blur_img = cv.GaussianBlur(gray_img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur_img)

canny = cv.Canny(image=blur_img, threshold1=125, threshold2=175)
cv.imshow('Canny Edges', canny)

# Finding contours
"""
cv.RETR_LIST :- returns all contours in the image
cv.RETR_EXTERNAL :- returns all exterior contours
cv.RETR_TREE :- returns all hierarchy contours


cv.CHAIN_APPROX_NONE :- Returns all contours found
cv.CHAIN_APPROX_SIMPLE :- Returns a compressed form of these contours, only including those that are simple and most important
"""


"""
Second way is using the `cv.threshold` function
Here, 125 is the threshold, meaning if a pixel has density above 125 it will be white and if it has below 125, it will be black
"""

# ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
# cv.imshow('ThreshHold', thresh)

contours, hierarchies = cv.findContours(image=canny, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!!!')


# Visualize contours
cv.drawContours(image=blank, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)