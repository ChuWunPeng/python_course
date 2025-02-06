import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('image/Photos/cats.jpg')
cv.imshow('Cats',img)


blank = np.zeros(img.shape[:2],dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)


mask = cv.bitwise_and(gray,gray,mask = circle)
cv.imshow('Mask',mask)

# GRayscale histogram

gray_hist = cv.calcHist([gray],[0], mask, [256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
plt.plot(gray_hist)

plt.show()

# Color Histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


colors = ('b','g','r')
for i,col in enumerate(colors):
    hist =  cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
    plt.legend(colors)

plt.show()







cv.waitKey(0)
cv.destroyAllWindows(0)