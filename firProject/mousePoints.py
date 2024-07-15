import cv2
import numpy as np

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


img = cv2.imread('Resources/cards.jpeg')



cv2.imshow("OriginalImage",img)
cv2.setMouseCallback("OriginalImage",mousePoints)

cv2.waitKey(0)