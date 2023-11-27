import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import cv2


def load_model():
    # Load the pre-trained ResNet50 model
    return ResNet50(weights='imagenet')

def prepare_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)

def prepare_image_from_array(img_array):
    # Resize and preprocess the image
    img = cv2.resize(img_array, (224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


def predict(model, processed_image):
    # Make a prediction and decode the result
    predictions = model.predict(processed_image)
    return decode_predictions(predictions, top=3)[0]

