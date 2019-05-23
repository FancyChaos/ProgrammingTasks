from flask import Flask, session, render_template, Blueprint, url_for, request,redirect, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("/home/maximilian/python/flask/upload/", filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/redirect')
def redirection():
    return redirect("http://www.google.de")

@app.route("/quiz", methods=("GET", "POST"))
def quiz():
    if request.method=="POST":
        answer = request.form["answer"]
        if answer == "7" or answer == "sieben":
            flash("Correct!")
        else:
            flash("Wrong answer try again...")

    return render_template('quiz.html')
