import cv2 as cv

img = cv.imread('Photos/face1.jpg')
cv.imshow('Original Image', img)

# 1. converting into gray scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scaled Image', gray_img)

# 2. Blur image
blur_img = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', blur_img)

# 3. Edge detector (if blurred img passed - less edge detected)
canny = cv.Canny(blur_img, threshold1=125, threshold2=175)
cv.imshow('Cany Edges', canny)

# 4.  Dilating the image
dilated = cv.dilate(src=canny, kernel=(7, 7), iterations=2)
cv.imshow('Dilated', dilated)

# 5. Eroded image
eroded = cv.erode(dilated, kernel=(3, 3), iterations=2)
cv.imshow('Eroded', eroded)

# 6. Resize image
resized = cv.resize(img, dsize=(500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 7. Cropping Image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)

