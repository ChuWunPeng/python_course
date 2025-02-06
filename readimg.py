#%% import library
import cv2 as cv
#%% Read image

img = cv.imread('image/Photos/cat.jpg')
cv.imshow('cat', img)
cv.waitKey(0)

#%% Reading Videos
# capture = cv.VideoCapture(0) 連接web cam

# capture = cv.VideoCapture('image/Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video',frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
# cv.waitKey(0)

