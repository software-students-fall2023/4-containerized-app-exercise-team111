"""
This module provides a Flask web application for processing images with object recognition.
It includes endpoints for processing images and interfacing with a database to store the results.
"""

import os
from flask import Flask, request, jsonify
from object_recognition import recognize_objects
from database_manager import DatabaseManager

app = Flask(__name__)

db_manager = DatabaseManager()


@app.route("/process", methods=["POST"])
def process_image():
    """
    Process an image and return object recognition results.
    Expects a POST request with an "image_path" in the JSON body.
    Returns JSON with the highest probability prediction and saves it to a database.
    """
    data = request.get_json()

    if not data or "image_path" not in data:
        return jsonify({"error": "No image path provided"}), 400

    image_path = data["image_path"]

    if not os.path.exists(image_path):
        return jsonify({"error": "Image file does not exist"}), 404

    try:
        predictions = recognize_objects(image_path)
        if not predictions:
            return jsonify({"error": "No predictions made"}), 500

        highest_prediction = max(predictions, key=lambda item: item[2])
        _, label, probability = highest_prediction
        highest_prediction_converted = {
            "label": label,
            "probability": float(probability),
        }

        db_manager.save_prediction(image_path, [highest_prediction_converted])

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5003")), debug=True)
