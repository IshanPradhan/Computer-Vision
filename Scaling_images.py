import cv2
import numpy as np

img = cv2.imread("Landscape.jpeg")
img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)

cv2.imshow("Original Image", img)
cv2.imshow("Scaling cubic intepolations", img_scaled)

img_scaled = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow("Scaling Skewed images", img_scaled)
cv2.waitKey(0)

cv2.destroyAllWindows()
