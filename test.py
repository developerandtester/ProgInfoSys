import cv2
import numpy as np
import pytesseract
from scipy import ndimage
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread('test.jpg')
cv2.imshow('OutputImage', image) #test


custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(image, config=custom_config))

h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('image', img)

#Coverting image to greyscale
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#grayscale picture needs to be applied#
canny = cv2.Canny(greyImage, 10, 155)
cv2.imshow('canny image', canny)

cv2.waitKey(0)
