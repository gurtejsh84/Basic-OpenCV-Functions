import cv2
import numpy as np

# The kernels is a matrix that helps to traverse in the img
kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "Resources/leena.png"
# Coverted img into grayscale
# img = cv2.imread(path,0)
# cv2.imshow("leena",img)

img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# The ksize is always in odd and if we increase it the intensity of blur increases
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
# imgBlur2 = cv2.GaussianBlur(imgGray,(7,7),0)

# by using canny we get the edges of the main part of our img
# Here the threshold parameters denotes the intensity
# if parameters are high ---> less lines
imgCanny = cv2.Canny(imgBlur,100,100)
imgCanny2 = cv2.Canny(imgBlur,200,200)

# Increses the thicknes of the edges in the canny img
# more no of iterations more the thickness of edges
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)

# erosion is the reverse of dilation
imgEroded = cv2.erode(imgDilate,kernel,iterations=1)

# By using dilation
# cv2.imshow("Gray",imgGray)
# cv2.imshow("Blur",imgBlur)
# cv2.imshow("Blur2",imgBlur2)
cv2.imshow("Canny",imgCanny)
# cv2.imshow("Canny2",imgCanny2)
cv2.imshow("Dilate",imgDilate)
cv2.imshow("erosion",imgEroded)

cv2.waitKey(0)