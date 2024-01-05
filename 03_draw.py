import cv2 as cv
import numpy as np

# Blank image
blank_img = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank image', blank_img)

# 1. Paint the image a certain color
# blank_img[200:300, 300:400] = 225,225,72
# cv.imshow('Colored image', blank_img)

# 2. Draw a Rectangle 
cv.rectangle(img=blank_img, pt1=(0,0), pt2=(blank_img.shape[1]//2, blank_img.shape[0]//2), color=(225, 0, 0), thickness=cv.FILLED)

# 3. Draw a circle
cv.circle(img=blank_img, center=(250, 250), radius=50, color=(225, 225, 72), thickness=cv.FILLED)

# 4. Draw a line
cv.line(img=blank_img, pt1=(0, 0), pt2=(250, 250), color=(225, 0, 225), thickness=3)

# 5. Write text
cv.putText(blank_img, text='Hello, I am Harsh Singh!!', org=(20, 375), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 225, 225), thickness=2)

# show the image
cv.imshow('Rectangle & Circle & Line & Text', blank_img)


cv.waitKey(0)