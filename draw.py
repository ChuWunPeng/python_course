import cv2 as cv
import numpy as np

blank  =  np.zeros((500,500,3),dtype = 'uint8')
img = cv.imread('Photos/cat.jpg')
cv.imshow('Blank',blank)
cv.imshow('cat', img)

# 1. Paint the image a certain color
# blank[200:300,300:400] = 0,255,0
# cv.imshow('Green',blank)


# 2. Draw a Rectangle
cv.rectangle(blank,(0,0), (250,250), (0,255,0), thickness = cv.FILLED)
cv.imshow('Rectangle',blank)

# 3. Draw a Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness = -1)
cv.imshow('Circle',blank)


# 4. Draw a Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),
thickness = 3)
cv.imshow('Line',blank)


# 5. Write text
cv.putText(blank,'Hello, my name is Truman',(0,400),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)