import cv2
import numpy as np

frameWidth = 350
frameHeight = 350
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

# We will be using HSV i.e Hue,Saturation ,Value
# Hue ---> color       In openCv hue has values from 0 to 179 i.e. total 180 values
# Saturation ---> how pure the color is
# Value ---> how bright the color is

# For detection we need (max,min) values of all Hue and Saturation and Value
# we have to play around them until we get the desired results
# So in order to so we get trackbar i.e. just a slider that moves back adn forth and changes its values

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

while True:

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Min","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("VALUE Min","HSV")
    v_max = cv2.getTrackbarPos("VALUE Max","HSV")
    print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)  # This mask will provide the values in our specified ranges from imgHsv
    result = cv2.bitwise_and(img,img, mask = mask)

    #Stacking the images to present them in an easy way
    # We can stack ony those images having same channels like 3 channels BGR or others
    # as mask img was not is same channels therefore coverting it to same as img and result channels i.e. BGR
    mask = cv2.cvtColor(mask , cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV Color Space",imgHsv)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Result",result)
    cv2.imshow("Horizaontal Stack",hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()