import cv2
import numpy as np
import matplotlib.pyplot as plt

# Code to perform linear contrast stretching on an image.
# Given an upper and lower intensity value, the values of the pixels in the image change value.

def display(image):
    plt.imshow(image, cmap = 'gray')
    plt.axis("off")
    plt.show()

image = cv2.imread("./imageBox/quantum_bad.jpg", 1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

a = input("Lower intensity value: ")
b = input("Upper intensity value: ")
a = int(a)
b = int(b)

imageIntensities = [image.max(), image.min()]

range = 1/(int(imageIntensities[1]) - int(imageIntensities[0]))
output = np.uint8(range * image * (b - a) + a)

display(output)
