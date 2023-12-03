import numpy as np
import cv2
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from database_manager import DatabaseManager

# This module provides functions for object recognition using the MobileNetV2 model.
model = MobileNetV2(weights='imagenet')


def preprocess_image(image_path):
    """
    Preprocesses an image for object recognition.

    Args:
        image_path (str): The file path of the image to be processed.

    Returns:
        numpy.ndarray: The preprocessed image.
    """
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    return np.expand_dims(img, axis=0)


def recognize_objects(image_path):
    """
    Recognizes objects in an image using the MobileNetV2 model.

    Args:
        image_path (str): The file path of the image in which objects are to be recognized.

    Returns:
        list: A list of tuples containing the recognized objects and their probabilities.
    """
    img = preprocess_image(image_path)
    preds = model.predict(img)
    return decode_predictions(preds, top=3)[0]
