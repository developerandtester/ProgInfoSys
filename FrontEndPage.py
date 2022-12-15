from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PythonBoys'
app.config['UPLOAD_FOLDER'] = 'UploadImages'

class UploadPicture(FlaskForm):
    file = FileField("Picture", validators=[InputRequired()])
    submit = SubmitField("Upload Picture")

@app.route("/", methods = ['GET',"POST"])
@app.route("/home", methods = ['GET',"POST"])
def home():
    # return "<h1>Number Plate Recognition System<h1>"
    form=UploadPicture()
    if form.validate_on_submit():
        file = form.file.data 
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "Picture has been uploaded."
    return render_template('/index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
