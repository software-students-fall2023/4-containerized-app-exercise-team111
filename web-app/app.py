from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='public')

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# URL of the machine-learning-client service
ML_CLIENT_URL = 'http://localhost:5003/process'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, file.filename))
    file.save(image_path)

    try:
        response = requests.post(ML_CLIENT_URL, json={'image_path': image_path})
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Other error occurred: {err}'}), 500


@app.route('/uploads/<filename>')
def uploaded_file(filename):

    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
