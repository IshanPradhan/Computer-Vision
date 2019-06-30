import cv2
import numpy as np

img = cv2.imread("landscape.jpeg")
cv2.imshow("Landscape", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
