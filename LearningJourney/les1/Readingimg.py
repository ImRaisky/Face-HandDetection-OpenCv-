import cv2 as cv

catimage = cv.imread('Photos/Cat.jpg')
pixels = catimage.size
dimensions = catimage.shape
print("number of pixels : ", pixels, "dimensions : ", dimensions)
cv.imshow("Raisky", catimage)

cv.waitKey(0)