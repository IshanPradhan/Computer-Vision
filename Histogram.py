import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("landscape.jpeg")

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.hist(img.ravel(), 256, [0, 256])    # ravel converts 2D array to 1D array

plt.show()

color = ("b", "g", "r")

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])

plt.show()

# cv2.imshow("Landscape", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
