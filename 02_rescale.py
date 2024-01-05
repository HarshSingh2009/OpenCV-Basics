import cv2 as cv

# Loading image
img = cv.imread('Photos/custom_pizza.jpeg')

# Displaying Image
cv.imshow('Pizza', img)


# Resizing Frame function
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    new_shape = (width, height)
    
    return cv.resize(frame, new_shape, interpolation=cv.INTER_AREA)


# resizing and showing image
resized_img = rescaleFrame(img, scale=2)
cv.imshow('Resized Pizza', resized_img)
cv.waitKey(0)


# read a video
capture = cv.VideoCapture('D:\MachineLearning\Deep Learning\OpenCV\Videos\harsh_intro.mp4')

while True:
    status, frame = capture.read()

    if status:
        frame_resized = rescaleFrame(frame, scale=0.5)

        cv.imshow('Video', frame)
        cv.imshow('Videom Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
