from flask import Flask, render_template, send_from_directory,url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')


#initialising Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PythonBoys'
app.config['UPLOADED_PHOTOS_DEST'] = 'UploadImages'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

#Create a function for Validation on submit button
class UploadForm(FlaskForm):
    photo=FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File Field  should not be empty.')
        ]
    )
    submit = SubmitField('Upload')
    

#Flask Route to send Uplooaded Image Path
@app.route('/UploadImages/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)
    
    
#Flask Route to index Page
@app.route('/index2.html', methods= ['GET','POST'])
def upload_image():
    form= UploadForm()
    #Code for cliking on submit
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        #Getting Absolute Path from Relative Path 
        file_abs_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
        #Sending the image to get OCR output
        ocr_output=ocr.ocr(file_abs_path, cls=False, det=False)
        #Finetuning the output for better readlibitliy
        res = ocr_output[0]
        PlateNo=''
        for line in res:
            PlateNo=line
        file_output ='The license plate number is '+PlateNo[0] + ' The accuracy of result is around ' + str((round(float(PlateNo[1]*100),2)))
    else:# First Time Page Loading
        file_url = None
        file_output = None
    #Return Index2 Page
    return render_template('index2.html', form = form, file_url = file_url,file_output=file_output)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port='8080')# To launch app from any IP configured and on Port 8080 reserved for flask on Azure
