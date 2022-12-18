# ProgInfoSys

The git link for the project is : https://github.com/developerandtester/ProgInfoSys


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


Prathamesh Vyas(10611964):

Researched on various OCR technologies like pytesseract and PaddleOCR. Then tested them on sample images while using OpenCV. But pytesseract gave us unaccurate results as seen in test.py file. So we went with Paddle. And then we thought we could implement a neural network using darknet which will capture the license plates from videos of traffic and track the plates on a moving car. But the neural network required GPU and larger time to train a model. So we decided to just go with OCR. 

My contribution was that I research the methods, implemented them. I helped create the backend file Frontend2.py, and helped deployed the project on Azure. 
Output comes with accuracy percentage
Programming via python to achieve project goal.

We used Microsoft Azure platform for deployment, which gave us a cloud environment to run our project. We used PaddleOCR and OpenCV to detect the license plates in the images and videos. We used a flask server to connect the front end and back end. We used HTML, CSS and JavaScript to design the front end of the project. We also used pandas and numpy libraries to store the information of the license plates. 

The output of our project is the license plate number with accuracy percentage. We were able to successfully detect the license plates in the images and videos with satisfactory accuracy.


Nitin:


I worked on a project that involved integrating image optimization methods with pytesseract. For this, I used the canny method for edge detection and tested it using a sample image. After testing it, I moved on to creating the index page for the frontend. After this, I implemented the software on Azure. 

To do that, I first created a virtual device on Azure and configured the SSH and DNS for the website. After this, I cloned the code from the Git repository and installed the packages and dependencies required for the project. After this, I deployed the code and tested it multiple times to ensure that it was working properly. 

Apart from the backend development, I also helped my team mates on the frontend development and resolved any issues regarding it. This helped us in improving the overall user experience of the website. After this, I helped them in deploying the code on the production server. 

Overall, this project helped me gain a lot of experience in developing software using OCR . It also helped me learn more about the various optimization techniques used for images and how to implement using CRNN (convolutional recurrent neural network). Additionally, I also got an opportunity to work with Azure and learn about its various features.




Licenses:

Flask:

BSD-3-Clause Source License
The BSD-3-Clause license applies to all files in the Flask repository and source distribution. This includes Flask’s source code, the examples, and tests, as well as the documentation.

Copyright 2010 Pallets

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Paddle:
Copyright (c) 2016 PaddlePaddle Authors. All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Tesseract:


   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



