import cv2
import numpy as np

# img: np.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)
# shrink_koeff = 2
# img_height, img_width, _ = img.shape
# img = cv2.resize(img, (img_width//shrink_koeff, img_height//shrink_koeff), cv2.INTER_NEAREST)

frameWidth = 640
frameHigh = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHigh)

def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask=cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("Orig", img)
    # cv2.imshow("mask", mask)
    print(*lower, *upper)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
