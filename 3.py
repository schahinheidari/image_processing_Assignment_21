import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt


im = cv.imread('3.jpg')

# Create a Figure and plot
f = plt.figure()

plt.imshow(np.rot90(im,2))
# plt.Show() with block=True would show the output when there is no interactive plot.
plt.show(block=False)
