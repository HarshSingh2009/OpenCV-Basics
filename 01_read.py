import cv2 as cv


# read an image


img = cv.imread('Photos/custom_pizza.jpeg')
cv.imshow('Pizza', img)
cv.waitKey(0)
cv.destroyAllWindows()


# read a video
capture = cv.VideoCapture('D:\MachineLearning\Deep Learning\OpenCV\Videos\harsh_intro.mp4')

while True:
    status, frame = capture.read()
    
    if status:
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()