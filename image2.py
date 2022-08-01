# https://www.geeksforgeeks.org/cartooning-an-image-using-opencv-python/

import cv2
import numpy as np
  
# reading image 
imgL = cv2.imread("/home/hus/Pictures/Vincent_image.jpg")
img = cv2.resize(imgL, None, fx = 0.75, fy = 0.75)

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                         cv2.THRESH_BINARY, 5, 5)
   
# Cartoonization
color = cv2.bilateralFilter(img, 15, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
   
   
cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Gray", gray)
cv2.imshow("Cartoon", cartoon)
cv2.imwrite("/home/hus/Pictures/Vincent_Cartoon.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
