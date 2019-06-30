import cv2
import numpy as np

img = cv2.imread("landscape.jpeg")

M = np.ones(img.shape, dtype="uint8") * 75
print(M)

added = cv2.add(img, M)
cv2.imshow("Added", added)

subtracted = cv2.subtract(img, M)
cv2.imshow("Subtracted", subtracted)

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
