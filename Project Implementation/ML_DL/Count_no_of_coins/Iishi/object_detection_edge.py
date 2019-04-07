import cv2

img = cv2.imread('coins.png')
bilateral_filtered_image = cv2.bilateralFilter(img, 5, 175, 175)
edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
cv2.imshow('Edge', edge_detected_image)
cv2.waitKey(0)

contours,h = cv2.findContours(edge_detected_image,1,2)
for cnt in contours:
  
  cv2.drawContours(img,[cnt],0,(0,255,0),1)
 

cv2.imshow('Objects Detected',img)
cv2.waitKey(0)