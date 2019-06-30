import cv2

img = cv2.imread("galaxy.jpg", 0)

# 0 means greyscale image
# 1 means image in rgb format
# -1  for transparency

# print(type(img))

print(img)    # This will display image in 3D array format

print(img.shape)   # Shows height and width of image

print(img.ndim)    # shows the number of dimension in the image

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))   # tuple is width by height

cv2.imshow("Galaxy", resized_image)   # Displays the image, we have to specify key else it will
                                      # disappear in nanoseconds

cv2.imwrite("Galaxy_written.jpg", resized_image)
cv2.waitKey(0)  # 0 means it will wait for user to press a button
                # else pass a number>0 which means time in milliseconds
