import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scaled', gray)

# blank = np.zeros(img.shape[:2], dtype='uint8')

# mask = cv.circle(img=blank, center=(img.shape[1]//2, img.shape[0]//2), radius=100, color=225, thickness=-1)
# cv.imshow('Mask', mask)


# # Gray scale histogram
# gray_hist = cv.calcHist([gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])

# plt.figure(figsize=(8, 8))
# plt.title('Grayscaled Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(img=blank, center=(img.shape[1]//2, img.shape[0]//2), radius=100, color=225, thickness=-1)
cv.imshow('Mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)


plt.figure(figsize=(8, 8))
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist(images=[img], channels=[i], mask=mask, histSize=[256], ranges=[0, 256])
    plt.plot(hist, c=col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)