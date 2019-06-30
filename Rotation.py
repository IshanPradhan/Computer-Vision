import cv2
import numpy as np

image= cv2.imread("Trump.jpg")

height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 60, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Trump", image)
cv2.imshow("Rotated image", rotated_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
