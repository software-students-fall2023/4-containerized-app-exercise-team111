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
ML_CLIENT_URL = "http://localhost:5003/process"
MONGO_URI = "mongodb://localhost:27017"
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

    requests.post(ML_CLIENT_URL, json={"image_path": image_path}, timeout=10)
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]

    # Fetch all predictions from the database
    all_predictions = []
    for document in db["predictions"].find():
        if "predictions" in document:
            all_predictions.append(document["predictions"])

    # Return the current result and all predictions
    return jsonify(
        {
            "all_predictions": all_predictions,
        }
    )


@app.route("/predictions", methods=["GET"])
def list_predictions():
    """
    Retrieve all predictions from the database and return them as a JSON list.
    """
<<<<<<< HEAD
    print("Flask App CWD:", os.getcwd())
    return send_from_directory(UPLOAD_FOLDER, filename)
=======
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]

    predictions = []
    for document in db.results.find():
        # Assuming 'result' field in each document contains prediction data
        prediction_data = document.get("result")
        if prediction_data:
            predictions.append(prediction_data)

    return jsonify(predictions)
>>>>>>> 9727784d106c658bf93dc9e4606086b723e6c65c



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8001")), debug=True)
