import traceback

from flask import Flask, request, jsonify
from object_recognition import recognize_objects
from database_manager import DatabaseManager
import os

app = Flask(__name__)


db_manager = DatabaseManager()


@app.route('/process', methods=['POST'])
def process_image():
    data = request.get_json()

    if not data or 'image_path' not in data:
        return jsonify({'error': 'No image path provided'}), 400

    image_path = data['image_path']

    if not os.path.exists(image_path):
        return jsonify({'error': 'Image file does not exist'}), 404

    try:
        predictions = recognize_objects(image_path)
        highest_prediction = max(predictions, key=lambda item: item[2])
        _, label, probability = highest_prediction
        highest_prediction_converted = {
            'label': label,
            'probability': float(probability)
        }

        result_id = db_manager.save_prediction(image_path, [highest_prediction_converted])
        return jsonify({'result_id': str(result_id), 'prediction': highest_prediction_converted})
    except Exception as e:
        traceback_str = traceback.format_exc()
        app.logger.error(traceback_str)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
