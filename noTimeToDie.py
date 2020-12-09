#Matting is the process of extracting foreground object from an image.
#Chroma Keying is the process by which a specific colour (chroma) is replaced
#with a different element. These colour components aren't found in skin tones thus they can
#easily be removed from media.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(image):
    plt.imshow(image)
    plt.axis("off")
    plt.show()

if(__name__ == "__main__"):
    image = cv2.imread("./imageBox/fg.jpg", 1)
    background = cv2.imread("./imageBox/bg.jpg", 1)
    image = cv2.resize(image, (1280, 720))
    background = cv2.resize(background, (1280, 720))
    #loads the images in the BGR colourspace and resizes them to 1280 x 720
    display(image)

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb_background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
    #convers from the BGR colourspace to the RBG colourspace
    display(rgb_image)

    lowerThreshold_green = np.array([0, 200, 0])
    upperThreshold_green = np.array([200, 255, 200])
    #Setting thresholds between which the value in the mask will be 0

    mask = cv2.inRange(rgb_image, lowerThreshold_green, upperThreshold_green)
    display(mask)
    #masking the green background (it has a value of 0)

    masked_image = rgb_image
    masked_image[mask != 0] = np.zeros(3)
    #Setting other pixel intensity values to [0,0,0] to add the chroma foreground to a new background.
    display(masked_image)

    display(background + masked_image)
    #The final chroma keyed image.
