import cv2 as cv


img = cv.imread('Photos/cats.jpg')
cv.imshow('Original BGR image', img)

# ---------- Blurring Method 1: AVERAGING --------- (finds average of surrounding pixels)
average = cv.blur(src=img, ksize=(3, 3))
cv.imshow('Average Blur', average)

# ---------- Blurring Method 2: Gaussian --------- (less blur than averaging, but more natural) - (each pixel has weights assigned, whose average is taken up)
gaussian = cv.GaussianBlur(src=img, ksize=(3, 3), sigmaX=0)
cv.imshow('Gaussian Blur', gaussian)

# ---------- Blurring Method 3: Median --------- (computes median of the surrounding pixels) - (more effective in reducing noise)
median = cv.medianBlur(src=img, ksize=3)
cv.imshow('Median Blur', median)

# ---------- Blurring Method 3: Bilateral --------- (most effective, the best!!)
bilateral = cv.bilateralFilter(src=img, d=30, sigmaColor=35, sigmaSpace=35)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)