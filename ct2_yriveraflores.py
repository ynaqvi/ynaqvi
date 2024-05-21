import numpy as np
import cv2

img = cv2.imread('kitten.jpg')

#print(img)

#Exploring the image attributes
print('Shape of the image: {}'.format(img.shape))

print('Image Height: {}'.format(img.shape[0]))

print('Image Width: {}'.format(img.shape[1]))

print('Image Dimension: {}'.format(img.ndim))

#Splitting the channels
(B, G, R) = cv2.split(img)

#Show individual channels
cv2.imshow("RED", R)
cv2.imshow("BLUE", B)
cv2.imshow("GREEN", G)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Merge channels into one image

merge_kitty = cv2.merge([B, G, R])
cv2.imshow("Merged Kitty", merge_kitty)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Visualization of the channels
zeros = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.imshow("Green", cv2.merge([zeros, G, zeros]))

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))

cv2.waitKey(0)
