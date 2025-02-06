import cv2 as cv

# 1. Convert image to grayscale
img = cv.imread('image/Photos/park.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.imshow('Image', img)

# Blur an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# 2. Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# 3. Dilating the image
dilated = cv.dilate(canny,(3,3),iterations = 3)
cv.imshow('Dilated',dilated)

# 4. Eroding
eroded = cv.erode(dilated,(3,3),iterations = 3)
cv.imshow('Eroded',eroded)

# 5. Resize
resized = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC )
cv.imshow('Resized',resized)

# 6. Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)
cv.destroyAllWindows()