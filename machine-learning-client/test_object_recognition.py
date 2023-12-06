"""
Module for testing the object recognition functionality.
"""

import sys
import os
import numpy as np
from unittest.mock import patch
from object_recognition import preprocess_image

# Adjusting sys.path to include the directory above, so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@patch("cv2.imread", return_value=np.zeros((224, 224, 3), dtype=np.uint8))
def test_preprocess_image(mock_imread):
    """
    Test the preprocess_image function to ensure it correctly processes images.
    """
    test_image_path = "tests/images/tiger_testImage.jpg"
    processed_image = preprocess_image(test_image_path)
    assert processed_image.shape == (1, 224, 224, 3)


@patch("keras.applications.mobilenet_v2.MobileNetV2")
def test_recognize_objects(mock_mobilenetv2):
    """
    Test the recognize_objects function using a mocked MobileNetV2 model.
    """
    # Create a mock model and set the predict method
    mock_model = mock_mobilenetv2.return_value
    mock_model.predict.return_value = "dummy_prediction"
    # Add testing logic here (e.g., call a function that uses MobileNetV2)
