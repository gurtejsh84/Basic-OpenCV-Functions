import cv2
import numpy as np

# By using dimensions we can oonly store black or white images
img = np.zeros((512,512))
# We can store colors in image by introducing channels to the image
img2 = np.zeros((512,512,3))
print(img2) #This prints matrix with (0.) value as we have not defined any datatype

img3 = np.zeros((512,512,3),np.uint8)
print(img3)

img3[:] = 255,0,0   # B,G,R

cv2.line(img2,(0,0),(100,100),(0,255,0),2)
cv2.rectangle(img2,(100,250),(200,350),(0,0,255),2)
cv2.rectangle(img2,(250,400),(300,600),(0,0,255),cv2.FILLED)
cv2.putText(img2,"Draw shapes",(75,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)
cv2.imshow("Image2",img2)
cv2.imshow("Image3",img3)

cv2.waitKey(0)