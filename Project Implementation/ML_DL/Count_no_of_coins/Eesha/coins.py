import imutils
import cv2
import argparse

image=cv2.imread("c2.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray, 30, 150)
thresh=cv2.threshold(gray, 225, 255,cv2.THRESH_BINARY_INV)[1]
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
output=image.copy()
i=0
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if(len(approx)<10):
        continue
    cv2.drawContours(output,cnt,-1,(0,0,0),3)
    i+=1

cv2.putText(output,"total coins = "+str(i), (10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
cv2.imshow("Contours",output)
cv2.waitKey(0)
cv2.destroyAllWindows()

