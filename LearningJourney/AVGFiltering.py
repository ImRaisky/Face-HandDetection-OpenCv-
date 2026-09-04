import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv


def callback():
    return

def AverageFiltering():
    imgPath = (r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\yamaha-yzf-R1-4k.jpg")
    img = cv.imread(imgPath)

    winName = "Raisky AvgFilter"
    cv.namedWindow(winName)

    T = cv.createTrackbar("Blur Value", winName, 1, 100, callback)

    height, width, channel = img.shape
    scale = 1/4
    height = int(height*scale)
    width = int(width*scale)

    img = cv.resize(img, (width, height))

    while True:
        if cv.waitKey(1) == ord("q"):
            break
        Trackvalue = cv.getTrackbarPos('Blur Value', winName)

        if Trackvalue == 0:
            FilteredImg = img
        else:
            FilteredImg = cv.blur(img, (Trackvalue, Trackvalue))
        cv.imshow(winName, FilteredImg)





    cv.waitKey(0)




AverageFiltering()