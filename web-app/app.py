import os
import requests
from flask import Flask, render_template, request, jsonify, send_from_directory


"""
This module sets up a Flask web application for uploading and processing images.
"""
app = Flask(__name__, static_folder='public')

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# URL of the machine-learning-client service
ML_CLIENT_URL = 'http://localhost:5003/process'


@app.route('/')
def index():
    """
    Render the index page of the web application.
    """
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    """
    Handle the image upload and send it to the machine learning client for processing.
    Returns a JSON response with the result or error message.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, file.filename))
    file.save(image_path)

    response = requests.post(ML_CLIENT_URL, json={'image_path': image_path}, timeout=10)
    response.raise_for_status()
    result = response.json()
    return jsonify(result)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Serve an uploaded file from the UPLOAD_FOLDER.
    """
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
