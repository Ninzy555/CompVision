import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

cv2.imshow('color', img)
print(img.size)
print(img.shape)

b, g, r = cv2.split(img)

# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('read', r)
# print(r)

# merge_img = cv2.merge([r, g, b])
# cv2.imshow('merge_img', merge_img)

# img_gray = cv2.imread('robot.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img_gray', img_gray)
img_filled: numpy.ndarray = img.copy()


for row in range(0,int(img.shape[0]/2)):
    for column in range(int(img.shape[1] / 2),int(img.shape[1])):
        img_filled[row, column] = (0,255,0)
# cv2.imshow('img_filled', img_filled)

# croped_img = img[int(img.shape[0] / 2):, 0:int(img.shape[1] / 2)]
croped_img = img[100:200, 1000:650]
cv2.imshow('croped_img', croped_img)

cv2.waitKey(0)
