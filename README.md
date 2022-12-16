# ProgInfoSys



*This is place holder for Prathamesh number 1*

*THIS IS A TEST COMMIT FROM NITIN*

*This is a test commit from Abhimanyu*


#Taking refference from OpenCV Documentation
CV2: OpenCV
OpenCV is an open source computer vision Library used for image processing. 
We have used this here to load the image and further process it to read the text from the image. 
We are converting the image to greysclay to apply the canny method over it.

Canny Method is used for edge detection. 

Overview: 

A license plate reader (LPR) is a device designed to automatically detect and record vehicle license plates. It consists of a camera, a processor, and a software package that can identify license plates. The camera captures an image of the license plate and the processor converts it into a digital format. The software package then uses algorithms to recognize the characters on the license plate and log the information.

Here, we are implementing a Optical character recognition using PaddleOCR which offers multilingual support 



Contribution: 

Abhimanyu Yadav: 
Studied pyteseract OCR with my group members and implemented conversion of a colour image to greyScale that was further used in the canny method for edge detection. Since pyteseract OCR was not giving good results even after enhancing images. We decided to use Paddle OCR in the backend. I implemented the front end using the Flask web framework. The front end has the following functionality - 
- Choose and upload an image File (number plate) from the local system.
- Validate if there is any file and the file type is IMAGE. 
- Submit the file for OCR to run.
- Display the image of the number plate
- Display the detected number plate characters and the accuracy of the result. 
To upload the file, I used the FileField function from the flask. 
To validate the file, I used validation such as FileAllowed, and FileRequired.
To submit the file, SubmitField was used.
We used index2.html to design the layout of the frontend page. 
We upload the image in flask form and then later send that information to the HTML page to display.



