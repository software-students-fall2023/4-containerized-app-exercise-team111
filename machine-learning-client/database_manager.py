from pymongo import MongoClient


class DatabaseManager:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.db = self.client['object_recognition_db']

    def save_prediction(self, image_path, predictions):
        collection = self.db['predictions']
        prediction_data = {
            'image_path': image_path,
            'predictions': predictions  # Expecting a list of dictionaries
        }
        result = collection.insert_one(prediction_data)
        return result.inserted_id

    def get_results(self):
        return list(self.db.results.find())
