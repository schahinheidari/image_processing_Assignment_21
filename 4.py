import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt



img = cv.imread('4.jpg', 0)
new = cv.resize(img,(400,400))


#read image as grey scale
img_grey = cv.imread('4.jpg', cv.IMREAD_GRAYSCALE)

# define a threshold, 160 is the middle of black and white in grey scale
thresh = 160

# threshold the image
img_binary = cv.threshold(img_grey, thresh, 255, cv.THRESH_BINARY)[1]

#save image
cv.imwrite('blackWhite.png',img_binary) 
