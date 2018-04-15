import cv2
import numpy as np

image = cv2.imread('./image/korea_bjj.PNG',cv2.IMREAD_COLOR)
image = cv2.resize(image, (0, 0), 2, .25, 0.5)
height, width = image.shape[:2]
# Make the grey scale image have three channels
image2 = cv2.imread('./image/as3.PNG',cv2.IMREAD_COLOR)
image2 = cv2.resize(image2, (width, height), 2, .25, 0.5)

numpy_vertical = np.vstack((image, image2))
numpy_horizontal = np.hstack((image, image2))

numpy_vertical_concat = np.concatenate((image, image2), axis=0)
numpy_horizontal_concat = np.concatenate((image, image2), axis=1)

cv2.imshow('Main', image)
cv2.imshow('Numpy Vertical', numpy_vertical)
cv2.imshow('Numpy Horizontal', numpy_horizontal)
cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()