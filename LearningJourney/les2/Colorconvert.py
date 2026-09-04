import cv2 as cv

img = cv.imread('../Ressources/Photos/Cat.jpg')
imgpixels = img.size
imgdimensions = img.shape
print("pixels : ", imgpixels, "dimensions : ", imgdimensions)


grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grey = cv.resize(grey, (600, 425))
greypixels = grey.size
greydimensions = grey.shape
print("pixels : ", greypixels, "dimensions : ", greydimensions)


cv.imshow("ٌRaisky", img)
cv.imshow("ٌRaisky_Grey", grey)
cv.waitKey(0)