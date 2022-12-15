from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')

cr_img='in\Volkswagen-Vento-527913c.jpg_0006_0377_0362_0222_0059.png'
result = ocr.ocr(cr_img, cls=False, det=False)
print(result)