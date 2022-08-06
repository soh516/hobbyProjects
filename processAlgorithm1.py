# https://www.geeksforgeeks.org/cartooning-an-image-using-opencv-python/

import cv2
import numpy as np
  
def algorithm1(inputFile):
    # reading image 
    imgL = cv2.imread(inputFile)
    scale = 0.25
    img = cv2.resize(imgL, None, fx = scale, fy = scale)

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
    #cv2.imwrite("/home/hus/Pictures/" + name + "_edge1.jpg", edges)
    #cv2.imwrite("/home/hus/Pictures/" + name + "_cartoon1.jpg", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
