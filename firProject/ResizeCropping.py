import cv2
# In openCV , +x is towards right direction and +y is towards down direction

path = "Resources/leena.png"
img = cv2.imread(path)
print(img.shape)
# (height,width,channels)   channels i.e BGR or other

width,height = 300,300
imgResize = cv2.resize(img,(width,height))

# img[height,width]
imgCropped = img[200:380,0:518]
imgCropResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))

cv2.imshow("Road",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.imshow("CroppedResized",imgCropResize)


cv2.waitKey(0)
