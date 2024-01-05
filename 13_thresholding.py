import cv2 as cv


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# --------- Simple Thresholding ---------
"""
if image value below threshold then assigns 0, else 1
"""

threshold, thresh = cv.threshold(gray, thresh=130, maxval=255, type=cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse converts white pixels to black and vice versa
threshold_inv, thresh_inv = cv.threshold(gray, thresh=130, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)


# --------- Adaptive Thresholding ----------
"""
Finds Threshold value on its own for a particular image
"""

adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Inverse

adaptive_thresh_inv = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=9)
cv.imshow('Adaptive Thresholding Invese', adaptive_thresh_inv)


cv.waitKey(0)