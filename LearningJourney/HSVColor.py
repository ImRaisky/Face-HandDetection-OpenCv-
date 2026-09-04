import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def SelectHsvColor():

    path = (r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\Cat.jpg")
    img = cv.imread(path)

    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    print(imgHSV[0, 0:4, 0:3])

    lowerrange = np.array([0, 0, 0])
    upperrange = np.array([17, 100, 100])

    mask = cv.inRange(imgHSV, lowerrange, upperrange)

    cv.imshow("Real image", img)
    cv.imshow("Test image", mask)
    cv.waitKey(0)


SelectHsvColor()