import cv2
import numpy as np

image = cv2.imread("Black Squares.png")

cv2.imshow("Original Image", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Grayscale image", gray)

# since contours require gray scale image we converted the image to gray scale image

edged = cv2.Canny(gray, 30, 200)
cv2.imshow("Canny Edges after contouring", edged)

(hierarchy, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Number of contours found: " + str(len(cnts)))

cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)
cv2.imshow("After applying contours", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
