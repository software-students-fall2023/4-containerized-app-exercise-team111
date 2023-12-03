"""
# This module provides a DatabaseManager class for interacting with a MongoDB database.
"""

from pymongo import MongoClient


class DatabaseManager:
    """
    A class to manage database operations for the object recognition system.

    Attributes:
        client (MongoClient): A MongoClient object for interacting with the MongoDB server.
        db (Database): A reference to the MongoDB database.
    """

    def __init__(self, uri="mongodb://localhost:27017/"):
        """
        Initializes the DatabaseManager with a MongoDB connection.
        """
        self.client = MongoClient(uri)
        self.db = self.client['object_recognition_db']

    def save_prediction(self, image_path, predictions):
        """
        Saves a prediction result to the database.

        Args:
            image_path (str): The path of the image for which predictions are made.
            predictions (list): A list of prediction results, each being a dictionary.

        Returns:
            ObjectId: The ID of the inserted document in the database.
        """
        collection = self.db['predictions']
        prediction_data = {
            'image_path': image_path,
            'predictions': predictions  # Expecting a list of dictionaries
        }
        result = collection.insert_one(prediction_data)
        return result.inserted_id

    def get_results(self):
        """
        Retrieves all prediction results from the database.

        Returns:
            list: A list of all prediction results stored in the database.
        """
        return list(self.db['predictions'].find())
