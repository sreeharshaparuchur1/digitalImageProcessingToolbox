#Quantising digital images.
#This is done to reduce the colourspace of the image, ideally for storing purposes.
#This method also reduces the noise in the image and the variance.
#Usually images are 8 bit images, that is each pixel can have a 256 possible values rainging from 0-255.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(image):
    plt.imshow(image, cmap = 'gray')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    image = cv2.imread("./imageBox/007_test1.png", 0)
    bits = input("Number of bits to quantise the image to: ")
    bits = int(bits)

    levels = 1
    multi = 2
    while(bits > 0):
        if(bits & 1 == 1):
            levels = levels * multi
        multi = multi * multi
        bits = bits >> 1

    print(levels)
    dim = image.shape
    print(dim)
    for i in range(dim[0]):
        for j in range(dim[1]):
            image[i][j] = (image[i][j] * levels) // 255

    display(image)
