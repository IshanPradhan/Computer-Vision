import cv2
import numpy as np

img = cv2.imread("openCV.jpg")
cv2.imshow("openCV", img)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Eroded image", erosion)

dialation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dialated image", dialation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

cv2.waitKey(0)

cv2.destroyAllWindows()
