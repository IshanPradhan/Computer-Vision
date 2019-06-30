import cv2
import numpy as np

template = cv2.imread("star.png")
cv2.imshow("Original image", template)

target = cv2.imread("target.png")
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
cv2.imshow("Target Image", target)

ret1, thresh1 = cv2.threshold(template, 127, 255, 0)
ret2, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

_, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

template_contour = contour[1]

contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv2.matchShapes(template_contour, c, 1, 0.0)
    print(match)
    if match < 0.15:
        closest_match = c
    else:
        closest_match = []

cv2.drawContours(target, [closest_contour], -1, (0, 255, 0), 2)
cv2.imshow("Output", target)

cv2.waitKey(0)
cv2.destroyAllWindows()