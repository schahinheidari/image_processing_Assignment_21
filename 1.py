import cv2 as cv

img = cv.imread("Black_photo.jpg")
new_img = cv.resize(img, (800, 800))

for i in range(0,800,100):
    for j in range(0,800,100):
        if ((i+j)/4)%2 == 0:
            new_img[i:i+100,j:j+100] = 255
        else:
            new_img[i:i+100,j:j+100] = 0


cv.imwrite("result.jpg", new_img)
cv.imshow("output", new_img)
cv.waitKey()


