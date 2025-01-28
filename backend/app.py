from flask import Flask, request, render_template, send_from_directory
import os
import subprocess
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Unzip if necessary
        if zipfile.is_zipfile(filepath):
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(app.config['UPLOAD_FOLDER'])
            os.remove(filepath)

        # Run Foldseek
        result_file = run_foldseek(filepath)

        return send_from_directory(RESULTS_FOLDER, result_file)

def run_foldseek(filepath):
    # Command to create database and run Foldseek
    db_path = os.path.join(RESULTS_FOLDER, 'foldseek_db')
    os.makedirs(db_path, exist_ok=True)
    subprocess.run(['foldseek', 'createdb', filepath, db_path])
    result_file = 'results.tsv'
    subprocess.run(['foldseek', 'search', filepath, db_path, os.path.join(RESULTS_FOLDER, result_file)])
    return result_file

if __name__ == '__main__':
    app.run(debug=True)
