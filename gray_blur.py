import cv2 as cv

img  = cv.imread('cat.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img,(21,21),0)

cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.waitKey(0)