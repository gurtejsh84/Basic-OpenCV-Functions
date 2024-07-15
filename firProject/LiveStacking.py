import cv2
import numpy as np
import StackingImagesTest
# from other import  StackingImagesTest


frameWidth = 640
frameHeight = 100

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
while True:
    sucess,img = cap.read()
    cv2.imshow("Video",img)

    kernel = np.ones((5, 5), np.uint8)
    print(kernel)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilate, kernel, iterations=2)

    StackedImages = StackingImagesTest.stackImages(0.8,([img,imgGray,imgBlur],[imgCanny,imgDilate,imgEroded]))
    cv2.imshow("StackedImages",StackedImages)

    # cv2.imshow("Gray",imgGray)
    # cv2.imshow("Blur",imgBlur)
    # cv2.imshow("Canny", imgCanny)
    # cv2.imshow("Dilate", imgDilate)
    # cv2.imshow("erosion", imgEroded)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break