import cv2 as cv
import numpy as np

image = cv.imread('/home/shahin/Desktop/Sajjad project/Assignment-21/image_processing_Assignment_21/images/5.jpg', 0)

#resize an image
img = cv.resize(image,(400,400))

# In terms of coordinates, it means the line will start on point (x=100, y=0) and end on point (x=0, y=100). 
# We are going to draw this line in black (B=0, G=0, R=0) and with a thickness of 15 pixels.
cv.line(img, (100,0), (0, 100), (0,0,0), 15)

cv.imwrite("/home/shahin/Desktop/Sajjad project/Assignment-21/image_processing_Assignment_21/images/imageWithLine.jpg", img)
cv.imshow("output",img)
cv.waitKey()