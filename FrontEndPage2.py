from flask import Flask, render_template, send_from_directory,url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PythonBoys'
app.config['UPLOADED_PHOTOS_DEST'] = 'UploadImages'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo=FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File Field  should not be empty.')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/', methods= ['GET','POST'])

@app.route('/UploadImages/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)
    

def upload_image():
    form= UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    return render_template('index2.html', form = form, file_url = file_url)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port='8080')
