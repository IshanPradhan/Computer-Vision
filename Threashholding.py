import cv2
import numpy as np

img = cv2.imread("apple.jpg")
cv2.imshow("Original Image", img)

# Values between 127 goes to zero(Black) everythin above goes to white
ret, thres1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("1 Threshold Binary", thres1)

ret, thres2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("2 Threshold Binary Inverse", thres2)
cv2.waitKey(0)

ret, thres3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("3 Threshold Trunc", thres3)
cv2.waitKey(0)

ret, thres4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("4 Threshold Torezo", thres4)
cv2.waitKey(0)

ret, thres5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("5 Threshold Torezo Inverse", thres5)

cv2.waitKey(0)
cv2.destroyAllWindows()
