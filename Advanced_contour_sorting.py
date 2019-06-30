import cv2
import numpy as np


def x_cord_contour(cnts):
    # returns the x-coordinate of contour centroid
    if cv2.contourArea(cnts) > 10:
        M = cv2.moments(cnts)
        return int(M["m00"]/M["m10"])


def label_contour(img, c, i):
    M = cv2.moments(c)
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])
    cv2.circle(img, (cx, cy), 10, (0, 0, 255), -1)
    return img


img = cv2.imread("Sorting_contours.png")
# cv2.imshow("Original image", img)
original_image = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 200)

(hierarchy, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print("Number of contours found: "+str(len(cnts)))

cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

cv2.waitKey(0)

for i, c in enumerate(cnts):
    orig = label_contour(img, c, i)

cv2.imshow("Contour Centers", img)
cv2.waitKey(0)

contours_left_to_right = sorted(cnts, key=x_cord_contour, reverse=False)

for i, c in enumerate(contours_left_to_right):
    cv2.drawContours(original_image, [c], -1, (0, 0, 255), 3)
    M = cv2.moments(c)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.putText(original_image, str(i+1), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Left to Right", original_image)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)

    cropped_contour = original_image[y:y+w, x:x+h]
    image_name = "Output Shape Number " + str(i+1) + ".jpeg"
    print(image_name)
    cv2.imwrite(image_name, cropped_contour)

cv2.destroyAllWindows()
