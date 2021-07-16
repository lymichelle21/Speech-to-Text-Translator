import os
import glob
from flask import Flask, request, url_for, redirect, render_template, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.wav', '.aiff', '.flac']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
         return redirect(url_for('transcribe'))
    if request.method == 'POST':
         return redirect(url_for('learn'))
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index.html'))

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

@app.route('/uploads/<filename>')
def upload(filename):
    print("GOT FILE ", filename)
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
