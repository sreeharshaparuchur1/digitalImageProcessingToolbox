import cv2
import numpy as np
import matplotlib.pyplot as plt

#The point of this is to find out the corruption procedure that takes image
# mallory to image mallory_corrupt.

def display(image):
    plt.imshow(image, cmap = 'gray')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    image = cv2.imread("./imageBox/mallory.jpg", 0)
    imageCorrupt = cv2.imread("./imageBox/mallory_corrupt.jpg", 0)
    dim = imageCorrupt.shape
    max = 0
    print(dim)

    for i in range(dim[0]):
        for j in range(dim[1]):
            #print(imageCorrupt[i][j])
            if imageCorrupt[i][j] > max:
                max = imageCorrupt[i][j]

    level = 1
    counter = 0
    while(level < max):
        level = level << 1
        counter += 1

    #counter tells us the number of bits the quantisation was done on.

    display(imageCorrupt)
    print(level)
    print(counter)
