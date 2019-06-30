import cv2
import numpy as np

img = cv2.imread("landscape.jpeg")
cv2.imshow("Original Image", img)

# Sum of all elements of matrix should be 1

kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])

sharpened = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
