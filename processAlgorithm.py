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

def algorithm2(inputFile):

    # reading image
    scale = 0.25
    imgL = cv2.imread(inputFile)
    img = cv2.resize(imgL, None, fx = scale, fy = scale)

    # Apply some Gaussian blur on the image
    img_gb = cv2.GaussianBlur(img, (7, 7) ,0)
    # Apply some Median blur on the image
    img_mb = cv2.medianBlur(img_gb, 5)
    # Apply a bilateral filer on the image
    img_bf = cv2.bilateralFilter(img_mb, 5, 80, 80)

    # Use the laplace filter to detect edges
    img_lp_im = cv2.Laplacian(img, cv2.CV_8U, ksize=5)
    img_lp_gb = cv2.Laplacian(img_gb, cv2.CV_8U, ksize=5)
    img_lp_mb = cv2.Laplacian(img_mb, cv2.CV_8U, ksize=5)
    img_lp_al = cv2.Laplacian(img_bf, cv2.CV_8U, ksize=5)

    # Convert the image to greyscale (1D)
    img_lp_im_grey = cv2.cvtColor(img_lp_im, cv2.COLOR_BGR2GRAY)
    img_lp_gb_grey = cv2.cvtColor(img_lp_gb, cv2.COLOR_BGR2GRAY)
    img_lp_mb_grey = cv2.cvtColor(img_lp_mb, cv2.COLOR_BGR2GRAY)
    img_lp_al_grey = cv2.cvtColor(img_lp_al, cv2.COLOR_BGR2GRAY)

    # Remove some additional noise
    blur_im = cv2.GaussianBlur(img_lp_im_grey, (5, 5), 0)
    blur_gb = cv2.GaussianBlur(img_lp_gb_grey, (5, 5), 0)
    blur_mb = cv2.GaussianBlur(img_lp_mb_grey, (5, 5), 0)
    blur_al = cv2.GaussianBlur(img_lp_al_grey, (5, 5), 0)

    # Apply a threshold (Otsu)
    _, tresh_im = cv2.threshold(blur_im, 245, 255,cv2.THRESH_BINARY +  cv2.THRESH_OTSU)
    _, tresh_gb = cv2.threshold(blur_gb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, tresh_mb = cv2.threshold(blur_mb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, tresh_al = cv2.threshold(blur_al, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    inverted_original = cv2.subtract(255, tresh_im)
    inverted_GaussianBlur = cv2.subtract(255, tresh_gb)
    inverted_MedianBlur = cv2.subtract(255, tresh_mb)
    inverted_Bilateral = cv2.subtract(255, tresh_al)

    # Reshape the image
    img_reshaped = img.reshape((-1,3))
    # convert to np.float32
    img_reshaped = np.float32(img_reshaped)
    # Set the Kmeans criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # Set the amount of K (colors)
    K = 8
    # Apply Kmeans
    _, label, center = cv2.kmeans(img_reshaped, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)# Covert it back to np.int8
    center = np.uint8(center)
    res = center[label.flatten()]
    # Reshape it back to an image
    img_Kmeans = res.reshape((img.shape))

    div = 64
    img_bins = img // div * div + div // 2

    # Convert the mask image back to color
    inverted_Bilateral = cv2.cvtColor(inverted_Bilateral, cv2.COLOR_GRAY2RGB)
# Combine the edge image and the binned image
    cartoon_Bilateral = cv2.bitwise_and(inverted_Bilateral, img_bins)# Save the image
    cv2.imshow("Original", img)
    cv2.imshow("Edges", inverted_Bilateral)
    #cv2.imshow("Grey", tresh_al)
    cv2.imshow("Cartoon", cartoon_Bilateral)
    #cv2.imwrite("/home/hus/Pictures/" + name + "_edge.jpg", inverted_Bilateral)
    #cv2.imwrite("/home/hus/Pictures/" + name + "_cartoon.jpg", cartoon_Bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
