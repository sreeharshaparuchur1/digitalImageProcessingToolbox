#Image planes
#Given an 8 bit image, we decompose the image into 8 individual images known as bitplanes. These images are greyscaled.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(image):
    plt.imshow(image)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    #name = input("Image name: ")
    #bits = input("Number of bits to quantise the image to: ")
    #bits = int(bits)
    image = cv2.imread("./imageBox/007_test2.png", 0)
    display(image)
    dim = image.shape
    print(dim)

    bitPlane1 = []
    #Least significant bit
    bitPlane2 = []
    bitPlane3 = []
    bitPlane4 = []
    bitPlane5 = []
    bitPlane6 = []
    bitPlane7 = []
    bitPlane8 = []
    #Most significant bit

    #Generating bit planes
    for i in range(dim[0]):
        for j in range(dim[1]):
            values = [0, 0, 0, 0, 0, 0, 0, 0]
            pos = 7
            while image[i][j] > 0:
                if image[i][j] & 1 == 1:
                    values[pos] = 1
                image[i][j] = image[i][j] >> 1
                pos -= 1
            bitPlane1.append(values[7])
            bitPlane2.append(values[6])
            bitPlane3.append(values[5])
            bitPlane4.append(values[4])
            bitPlane5.append(values[3])
            bitPlane6.append(values[2])
            bitPlane7.append(values[1])
            bitPlane8.append(values[0])

    bitPlane1 = np.array(bitPlane1).reshape(dim[0], dim[1])
    bitPlane2 = np.array(bitPlane2).reshape(dim[0], dim[1])
    bitPlane3 = np.array(bitPlane3).reshape(dim[0], dim[1])
    bitPlane4 = np.array(bitPlane4).reshape(dim[0], dim[1])
    bitPlane5 = np.array(bitPlane5).reshape(dim[0], dim[1])
    bitPlane6 = np.array(bitPlane6).reshape(dim[0], dim[1])
    bitPlane7 = np.array(bitPlane7).reshape(dim[0], dim[1])
    bitPlane8 = np.array(bitPlane8).reshape(dim[0], dim[1])

    display(bitPlane1)
    display(bitPlane2)
    display(bitPlane3)
    display(bitPlane4)
    display(bitPlane5)
    display(bitPlane6)
    display(bitPlane7)
    display(bitPlane8)
