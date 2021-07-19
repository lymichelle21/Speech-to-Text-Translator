import os
import glob
import speech_recognition as sr
sr.__version__
'3.8.1'
from flask import Flask, request, url_for, redirect, render_template, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 7000 * 7000
app.config['UPLOAD_EXTENSIONS'] = ['.wav', '.aiff', '.aiff-c', '.flac']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

        if request.method == 'POST':
             return render_template('transcribe.html', transcript=transcript)
        if request.method == 'POST':
             return render_template('learn.html')

    return render_template('index.html', transcript=transcript)

'''
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
         return redirect(url_for('transcribe'))
    if request.method == 'POST':
         return redirect(url_for('learn'))
    return render_template("index.html")
'''

@app.route("/transcribe", methods=['POST', 'GET'])
def transcribe():
    if request.method == 'POST':
         return redirect(url_for('index'))
    print(glob.glob("uploads/*.wav"))
    return render_template("transcribe.html")


@app.route("/learn", methods=['POST', 'GET'])
def learn():
    if request.method == 'POST':
         return redirect(url_for('index'))
    return render_template("learn.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
