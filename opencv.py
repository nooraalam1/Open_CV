import cv2 as cv

img  = cv.imread('cat.jpg')
cv.imshow('img',img)
cv.waitKey(0)