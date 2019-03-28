import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.png')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('image',img)
cv2.imshow('threshold image',th)
cv2.waitKey(0)
contours,h = cv2.findContours(th,1,2)
for cnt in contours:
  cv2.drawContours(img,[cnt],0,(0,0,255),1)
cv2.imshow('Objects Detected',img)
cv2.waitKey(0)

cv2.destroyAllWindows()