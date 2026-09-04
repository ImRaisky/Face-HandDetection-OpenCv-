import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def EditTheImagePixel():
    img = cv.imread(r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\kittie.jpg") # read the image as BGR

    imgrgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    imgrgb[200:450, 300:600, 0] += 20

    plt.imshow(imgrgb)
    plt.show()
        
    cv.imshow("cat", cv.cvtColor(imgrgb, cv.COLOR_RGB2BGR))
    cv.waitKey(0)





EditTheImagePixel()