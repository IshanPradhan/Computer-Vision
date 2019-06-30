import cv2
import numpy as np

# img = cv2.imread("landscape.jpeg")

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
# cv2.imshow("Square", square)

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
# cv2.imshow("Ellipse", ellipse)

And = cv2.bitwise_and(square, ellipse)
cv2.imshow("And", And)

Or = cv2.bitwise_or(square, ellipse)
cv2.imshow("Or", Or)

Xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("Xor", Xor)

Not = cv2.bitwise_not(square)
cv2.imshow("Not", Not)

cv2.waitKey(0)
cv2.destroyAllWindows()

