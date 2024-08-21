# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# import os
# from image_recognition import classify_image, generate_description

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return "No file part"
#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"
#     if file:
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         predictions = classify_image(file_path)
#         description = generate_description(predictions)
#         return jsonify({"description": description})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Process the file (e.g., save it, perform image recognition, etc.)
    return jsonify({'message': 'File successfully uploaded'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
