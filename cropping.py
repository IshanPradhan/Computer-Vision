import cv2
import numpy as np

img = cv2.imread("Landscape.jpeg")

height, width = img.shape[:2]
start_row, start_column = int(height*0.25), int(width*0.25)
ending_row, ending_column = int(height*0.75), int(width*0.75)

cropped = img[start_row:ending_row, start_column:ending_column]

cv2.imshow("Original image", img)
cv2.imshow("Cropped image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
