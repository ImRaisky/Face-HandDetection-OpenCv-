import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def ImageHistogram():

    imgpath = (r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\Cat.jpg")
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)



    plt.imshow(imgRGB)
    plt.show()

    histR = cv.calcHist([imgRGB], [0], None, [256], [0, 256]) # calc every red color from 0 to 256 how many pixel have every value of it
    histG = cv.calcHist([imgRGB], [1], None, [256], [0, 256]) # calc every green color from 0 to 256 how many pixel have every value of it
    histB = cv.calcHist([imgRGB], [2], None, [256], [0, 256]) # calc every blue color from 0 to 256 how many pixel have every value of it

    print(histR)
    plt.plot(histR, "r")
    plt.plot(histG, "g")
    plt.plot(histB, "b")
    plt.show()







ImageHistogram()