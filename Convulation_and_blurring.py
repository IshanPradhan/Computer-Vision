import cv2
import numpy as np

img = cv2.imread("puppy.jpg")
cv2.imshow("puppy", img)

kernel_3X3 = np.ones((3, 3), np.float32)/9

# 3X3 Blurring

blurred = cv2.filter2D(img, -1, kernel_3X3)
# cv2.imshow("Blurred", blurred)

# 7X7 Blurring

kernel_7X7 = np.ones((7, 7), np.float32)/9

blurring = cv2.filter2D(img, -1, kernel_7X7)
# cv2.imshow("7X7 Blurring", blurring)

blur = cv2.blur(img, (3, 3))
cv2.imshow("Average Blur", blur)

gaussian = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow("Gaussian Blur", gaussian)

median = cv2.medianBlur(img, 3)
cv2.imshow("Median Blur", median)

bilateral = cv2.bilateralFilter(img, 9, 7, 5)
cv2.imshow("Bilateral Binding", bilateral)

dst = cv2.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 21)
cv2.imshow("Fast means de noising", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
