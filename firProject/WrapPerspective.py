import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpeg')

width,height = 250,350
pts1 = np.float32([[125,58],[243,34],[161,253],[285,228]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

# Convert the coordinates to integers
for x in range (0,4):
    center = (int(pts1[x][0]), int(pts1[x][1]))
    cv2.circle(img, center, 5, (0,0,255), cv2.FILLED)

cv2.imshow("Original image", img)
cv2.imshow("Warpped image", output)
cv2.waitKey(0)
