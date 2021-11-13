import random
import cv2
import numpy


def getContours(val):
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgContours, contours, -1,(255,0,0), 5, cv2.LINE_8, hierarchy)
            peri = cv2.arcLength(cnt, True,)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.rectangle(imgContours, (x,y),(x+w, y+h), (0,255,0), 5)
            conrer_amount = len(approx)
            if conrer_amount ==3:
                objectType = "Tri"
            elif conrer_amount == 4:
                ratio = w/float(h)
                if 0.98<ratio<1.02: objectType = "Four"
                else: objectType = "Rect"
            elif conrer_amount ==8:
                objectType = "Circle"
            else:
                objectType = "None"
            text_x = x + w//2 -20
            text_y = y + h//2
            cv2.putText(imgContours, objectType, (text_x, text_y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.8, (0,0,0), 1)
    cv2.imshow('imgContours', imgContours)


def thresh_callback(val):
    imgCanny = cv2.Canny(imgBlur1, val, val)

    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    drawing = numpy.zeros((imgCanny.shape[0],imgCanny.shape[1],3), numpy.uint8)
    for contour_index in range(len(contours)):
        color = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
        cv2.drawContours(drawing, contours, contour_index,color, 2, cv2.LINE_8, hierarchy)
    cv2.imshow('imgCanny', drawing)


img: numpy.ndarray = cv2.imread('shapes.png', cv2.IMREAD_COLOR)
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur1 = cv2.GaussianBlur(img, (3,3), 1)
imgCanny = cv2.Canny(imgBlur1, 255, 255)
getContours(imgCanny)

# Создаём окно
# wind_name = 'Img'
# cv2.namedWindow(wind_name)
# cv2.imshow(wind_name, img)
# max_thresh = 255
# init_thresh = 50
# cv2.createTrackbar("Canny thresh:", wind_name, init_thresh, max_thresh, thresh_callback)
# thresh_callback(init_thresh)

# cv2.imshow('origin', img)
# cv2.imshow('gray', imgGray)
# cv2.imshow('imgBlur1', imgBlur1)
# cv2.imshow('imgCanny', imgCanny)

cv2.waitKey(0)