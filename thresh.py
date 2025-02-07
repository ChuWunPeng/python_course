import cv2 as cv
import numpy as np


img = cv.imread("Photos/cats.jpg")
cv.imshow('Cats',img)

# img  = cv.medianBlur(img,7)
img = cv.GaussianBlur(img,(5,5),2)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
# Find contours
contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Create an empty mask
mask = np.zeros_like(gray)

# List all contour areas and filter by area > 2000
contour_areas = [(i, cv.contourArea(contour)) for i, contour in enumerate(contours) if cv.contourArea(contour) > 2000]
for i, area in contour_areas:
    print(f"Contour {i} area: {area}")
    # Draw each contour on the mask
    cv.drawContours(mask, [contours[i]], -1, 255, thickness=cv.FILLED)

# Apply the mask to the original image
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)

# Inverse Simple Thresholding
threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Simple Thresholded Image',thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,19,3)
cv.imshow('Adaptive Thresholded Image',adaptive_thresh)

# Adaptive Thresholding (Gaussian)
adaptive_thresh_gaussian = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,19,3)
cv.imshow('Adaptive Thresholded Image (Gaussian)',adaptive_thresh_gaussian)




cv.waitKey(0)