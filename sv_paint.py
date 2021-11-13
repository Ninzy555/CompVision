import cv2
import numpy as np

img = np.zeros((500,500,3), np.uint8)
img_height, img_width, _ = img.shape
print(img.shape)
# img[200:300, 100:300]= 255,0,0

cv2.line(img, (0,0), (img_height//2,img_width//2), (0,255,0), 3)
cv2.rectangle(img, (0,0), (img_height//2,img_width//2), (0,255,0), 3)
cv2.rectangle(img, (250,250), (img_height,img_width), (0,0,250), cv2.FILLED)
cv2.circle(img, (img_height//2,img_width//2), 50, (0,250,250), 3)
cv2.circle(img, (img_height//2,img_width//2), 10, (0,250,250), cv2.FILLED)
cv2.putText(img, 'Fortune', (280,125), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0,150,150),3 )
cv2.imshow("image", img)

cv2.waitKey(0)