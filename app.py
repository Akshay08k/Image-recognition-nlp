from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from image_recognition import classify_image, generate_description

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        predictions = classify_image(file_path)
        description = generate_description(predictions)
        return jsonify({"description": description})

if __name__ == "__main__":
    app.run(debug=True)