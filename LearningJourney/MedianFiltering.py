import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def medianfiltering():
    imgpath = (r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\many-cats.jpg")
    img = cv.imread(imgpath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)


    noisyimg = imgRGB.copy()
    noiseProb = 0.05
    noise = np.random.rand(noisyimg.shape[0], noisyimg.shape[1])