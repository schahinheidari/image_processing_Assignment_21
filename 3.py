import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt


im = cv.imread('3.jpg')

f = plt.figure()

plt.imshow(np.rot90(im,2))
plt.show(block=True)
