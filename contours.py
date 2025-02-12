import cv2 as cv
import numpy as np

img = cv.imread('Photos\cats.jpg')

cv.imshow('Cat',img)

blank = np.zeros(img.shape,dtype='uint8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Thresholding
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

dilated = cv.dilate(thresh,(3,3),iterations = 3)

canny = cv.Canny(dilated,125,175)
cv.imshow('Canny',canny)



contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)
