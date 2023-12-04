import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from keras.applications.mobilenet_v2 import MobileNetV2
import numpy as np
from unittest.mock import patch
from object_recognition import preprocess_image, recognize_objects

@patch('cv2.imread', return_value=np.zeros((224, 224, 3), dtype=np.uint8))
def test_preprocess_image(mock_imread):
    test_image_path = 'tests/images/tiger_testImage.jpg'
    processed_image = preprocess_image(test_image_path)
    assert processed_image.shape == (1, 224, 224, 3)

@patch('keras.applications.mobilenet_v2.MobileNetV2')
def test_recognize_objects(mock_mobilenetv2):
    # Create a mock model and set the predict method
    mock_model = mock_mobilenetv2.return_value
    mock_model.predict.return_value = 'dummy_prediction'


