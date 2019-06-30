import cv2
import numpy as np

image = cv2.imread("landscape.jpeg")
height, width = image.shape[:2]
quarter_height, quarter_width = height/4, width/4

#     |1 0 Tx|
# T = |0 1 Ty|

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
image_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Landscape", image)
cv2.imshow("Translated Image", image_translation)

print(T)

cv2.waitKey(0)

cv2.destroyAllWindows()
