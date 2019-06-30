import cv2
import numpy as np

img = cv2.imread("Buildings.jpeg", 0)
print(img.shape)

height, width = img.shape

sobel_x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow("Original", img)
cv2.waitKey(0)

cv2.imshow("Sobel X", sobel_x)
cv2.waitKey(0)

cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("sobel Or", sobel_or)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)
cv2.waitKey(0)

canny = cv2.Canny(img, 20, 170)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

cv2.destroyAllWindows()