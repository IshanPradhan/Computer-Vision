import cv2
import numpy as np

img = cv2.imread("landscape.jpeg")

# cv2.imshow("Landscape", img)

b, g, r = cv2.split(img)

# cv2.imshow("Red", r)
# cv2.imshow("Blue", g)
# cv2.imshow("Green", b)

merged_image = cv2.merge([r, g, b+100])

cv2.imshow("Merged Image", merged_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
