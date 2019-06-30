import cv2
import numpy as np


def contours_by_area(cnts):
    all_areas = []
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas


img = cv2.imread("Sorting_contours.png")
original_image = img

blank_image = np.zeros((img.shape[0], img.shape[1], 3))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 200)
# cv2.imshow("Canny edged", edged)
# cv2.waitKey(0)

(hierarchy, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of contours found: "+str(len(cnts)))

cv2.drawContours(blank_image, cnts, -1, (0, 255, 0), 3)
# cv2.imshow("Counters on blank image", blank_image)
# cv2.waitKey(0)

cv2.drawContours(img, cnts, -1, (255, 0, 0), 3)
# cv2.imshow("Contours on image", img)
# cv2.waitKey(0)

sorted_contours = sorted(cnts, key=cv2.contourArea, reverse=True)

print(contours_by_area(sorted_contours))

for c in sorted_contours:
    cv2.drawContours(original_image, [c], -1, (0, 0, 0), 3)
    cv2.waitKey(0)
    cv2.imshow("contours by area", original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
