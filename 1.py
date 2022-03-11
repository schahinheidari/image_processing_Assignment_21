import cv2 as cv

img = cv.imread("Black_photo.jpg")
new_img = cv.resize(img, (400, 400))

for i in range(400):
    for j in range(400):
        if i % 2 == 0:
            new_img[i,j] = 0
        elif j % 2 == 0:
            new_img[i,j] = 0
        else:
            new_img[i,j] = 255


cv.imwrite("result.jpg", new_img)
cv.imshow("output", new_img)
cv.waitKey()


