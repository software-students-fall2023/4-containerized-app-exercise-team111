"""
This module sets up a Flask web application for uploading and processing images.
"""

import os
import requests
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="public")

# Directory to save uploaded images
UPLOAD_FOLDER = "uploads/"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# URL of the machine-learning-client service
ML_CLIENT_URL = "http://machine-learning-client:5003/process"
MONGO_URI = "mongodb://mongodb:27017"
MONGO_DBNAME = "object_recognition_db"
@app.route("/")
def index():
    """
    Render the index page of the web application.
    """
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    """
    Handle the image upload and send it to the machine learning client for processing.
    Returns a JSON response with the result or error message.
    """
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    image_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, file.filename))
    file.save(image_path)

    response = requests.post(ML_CLIENT_URL, json={"image_path": image_path}, timeout=10)
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]

    # Assuming the result is stored with a reference to the image filename
    # Add appropriate query logic based on your database schema
    query_result = db.results.find_one({"image_file": file.filename})

    if query_result is None:
        return jsonify({"error": "Result not found for the uploaded image"}), 404

    # Assuming 'result' field in the document contains the desired information
    return jsonify(query_result["result"])


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    """
    Serve an uploaded file from the UPLOAD_FOLDER.
    """
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
