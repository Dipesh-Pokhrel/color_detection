# Importing Libraries
import numpy as np
import cv2

# Hue: 0-180, saturation:0-255, Value: 0-255
img = cv2.imread('test/blue/1-11.jpg')

# Convert BGR colorspace to HSV.
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Displaying Image:
#cv2.imshow('HSV Image',imgHSV)

# Extacting HSV channel from image:
cv2.imshow('Hue Channel',imgHSV[:,:,0])
cv2.imshow('Saturation Channel',imgHSV[:,:,1])
cv2.imshow('Value Channel',imgHSV[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()