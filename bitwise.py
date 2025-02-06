import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),(255,0,0),thickness = -1)

circle = cv.circle(blank.copy(),(200,200),200,(255,0,0),thickness = -1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# Bitwise AND
Bitwise_AND = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',Bitwise_AND)

# Bitwise OR
Bitwise_OR = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',Bitwise_OR)

# Bitwise XOR
Bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',Bitwise_XOR)

# Bitwise NOT
Bitwise_NOT = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT',Bitwise_NOT)





cv.waitKey(0)
cv.destroyAllWindows()


