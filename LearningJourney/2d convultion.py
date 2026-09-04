import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def BlurImage():
    path = (r"D:\current system\Python\firstone\Opencv\Tests\Ressources\Photos\yamaha-yzf-R1-4k.jpg") # the path of the image
    img = cv.imread(path) # read the image
    Resized = cv.resize(img, (1920, 1080)) # resize the image to 1920x1080

    kernel = np.ones((10, 10), np.float32()) / 100 # create a 10x10 kernel where every value is 1/100
    Filtered = cv.filter2D(Resized, -1, kernel) # apply the kernel on the image and create a new filtered image




    
    cv.imshow("Raisky", Resized) # show the original resized image
    cv.imshow("Resized", Filtered) # show the filtered image
    cv.waitKey(0)







BlurImage()