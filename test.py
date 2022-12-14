import cv2
import numpy as np
import pytesseract
from scipy import ndimage
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread('E:\DBS\Prog_Project\ProgInfoSys\in\Audi-A6-528818b.jpg_0000_0311_0286_0189_0044.png')
#cv2.imshow('OutputImage', image) #test
image2 = cv2.imread('test.jpg')
#d = pytesseract.image_to_data(image, output_type=Output.DICT)
d = pytesseract.image_to_string(image)
print(d)

print('Resolving Captcha')

def resolve(img):
	enhancedImage = enhance()
	return pytesseract.image_to_string(enhancedImage)

def enhance():
	img = cv2.imread('E:\DBS\Prog_Project\ProgInfoSys\in\Audi-A6-528818b.jpg_0000_0311_0286_0189_0044.png', 0)
	kernel = np.ones((2,2), np.uint8)
	img_erosion = cv2.erode(img, kernel, iterations=1)
	img_dilation = cv2.dilate(img, kernel, iterations=1)
	erosion_again = cv2.erode(img_dilation, kernel, iterations=1)
	final = cv2.GaussianBlur(erosion_again, (1, 1), 0)
	return final


captcha_text = resolve('E:\DBS\Prog_Project\ProgInfoSys\in\Audi-A6-528818b.jpg_0000_0311_0286_0189_0044.png')
# img2= enhance(resolve(image))
# cv2.imshow('image',img2)
extracted_text = captcha_text.replace(" ", "").replace("\n", "")
print("OCR Result => ", extracted_text)
print(extracted_text)
        
custom_config = r'--oem 3 --psm 6'
#print(pytesseract.image_to_string(image, config=custom_config))

h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

#cv2.imshow('image', img)

#Coverting image to greyscale
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#grayscale picture needs to be applied#
canny = cv2.Canny(greyImage, 10, 155)
#cv2.imshow('canny image', canny)

#print(pytesseract.image_to_string(canny, config=custom_config))
cv2.waitKey(0)
