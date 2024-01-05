import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')

cv.imshow('Person 1', img)

# ---------- Translation (shifting images) ----------
def translate(frame, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (frame.shape[1], frame.shape[0])
    return cv.warpAffine(src=frame, M=transMat, dsize=dimensions)

"""
-x : Left
+x : Right

-y : Up
+y : Down
"""

translated_img = translate(frame=img, x=100, y=-100)
cv.imshow('Translated', translated_img)

# ---------- Rotation (Rotating an image) ----------
def rotate(frame, angle: int, rotPoint: tuple = None):
    (height, width) = frame.shape[:2]

    if rotPoint is None:
        # Finding the center of the image
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(center=rotPoint, angle=angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(src=frame, M=rotMat, dsize=dimensions)

rotated_img = rotate(frame=img, angle=-45, rotPoint=(img.shape[1]//2, img.shape[0]//2))
cv.imshow('Rotated', rotated_img)


# ---------- Resize ----------
resized_img = cv.resize(img, dsize=(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized_img)


# ---------- Flipping ----------
"""
flipCode: 0 - Flip Vertically
flipCode: 1 - Flip Horizontal
flipCode: -1 - Flip Vertical & Horizontal
"""
flip_img = cv.flip(src=img, flipCode=-1)
cv.imshow('Flip', flip_img)


cv.waitKey(0)