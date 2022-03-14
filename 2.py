import cv2 as cv
import matplotlib.pyplot as plt

# create figure
fig = plt.figure(figsize=(200,200))
im1 = cv.imread('1.jpg')
im2 = cv.imread('2.jpg')
# setting values to rows and column variables

new1 = abs(255 - im1)
new2 = abs(255 - im2)
rows = 1
columns = 2

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(im1)
plt.axis('off')
plt.title("affichage première image")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(im2)
plt.axis('off')
plt.title("affichage deuxième image")



plt.show()