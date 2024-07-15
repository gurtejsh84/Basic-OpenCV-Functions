import cv2
import numpy as np
import StackingImagesTest

frameWidth = 350
frameHeight = 350
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

# To detect edges we will use the Kenny Edge Detector , it has 2 thresholds
#  so, we have to move them around until we get required values
# This is done using trackbars
def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",150,255,empty)
cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
cv2.createTrackbar("Area","Parameters",4000,30000,empty)

# cv2.RETR_EXTERNAL ---> this methods return only the extreme outer corners
# cv2.RETR_TREE -----> this method returns all the corners/contours and reconstructs a full hierarchy

# cv2.CHAIN_APPROX_NONE ----> this methos give the stored conrners without any approximation
# cv2.CHAIN_APPROX_SIMPLE ----> this methos compreses the values and we will get lesser no of values/corners
def getContours(img,imgContour):

    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(imgContour, contours, -1, (255,0,255), 7)

    # By doing the below thing we reduced noise from the image
    # as smaller objects having area <= 1000 are not drawn i.e. removed from image
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area","Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)

            # Now in order to get the corners ,firstly we need to have the arc length
            # Here the True means that the contour is closed
            peri = cv2.arcLength(cnt,True)
            # This will give us the length of the parameter and we will use this to approximate its shape
            # 0.02*peri ---> this means the resolution
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # This approx array will have certain amount of points and based on them we will predict the shape
            # The below will give the no of corners
            print(len(approx))

            x , y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+w+20 , y+h+20) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0,255,0) , 2 )
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+w+20 , y+h+45) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0,255,0) , 2 )



while True:
    success, img = cap.read()

    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)

    kernel = np.ones((5, 5), np.uint8)
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDilate,imgContour)

    imgStack = StackingImagesTest.stackImages(0.8, ([img, imgGray, imgCanny],[imgDilate,imgContour,imgContour]))

    cv2.imshow("Result",imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;