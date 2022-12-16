from flask import Flask, redirect, url_for,request, render_template,flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PythonBoys'
app.config['UPLOAD_FOLDER'] = 'UploadImages'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class UploadPicture(FlaskForm):
    photo = FileField(
        validators=[
        InputRequired(),
        FileAllowed(photos, 'Please upload a image'),
        ]   )
    submit = SubmitField("Upload Picture")

@app.route("/", methods = ['GET',"POST"])
@app.route("/home", methods = ['GET',"POST"])
def home():
    # return "<h1>Number Plate Recognition System<h1>"
    form=UploadPicture()
    if request.method == 'POST':
        file = request.files['file']
        if photos:
            filename = secure_filename(photos.filename)
            photos.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
    return render_template('/index.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
