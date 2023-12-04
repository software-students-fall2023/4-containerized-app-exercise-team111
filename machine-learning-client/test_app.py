"""
This module contains tests for the Flask app in the machine-learning-client.
"""

import os
import sys
import pytest
from unittest.mock import patch
import numpy as np

# Correcting the import order and removing unused imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask app.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("object_recognition.recognize_objects")
@patch("database_manager.DatabaseManager.save_prediction")
@patch("os.path.exists", return_value=True)  # Mocking file existence
@patch(
    "cv2.imread", return_value=np.zeros((224, 224, 3), dtype=np.uint8)
)  # Mocking image reading with a dummy array
def test_process_image(
    mock_recognize_objects, mock_save_prediction, mock_exists, mock_imread, client
):
    """
    Test the process_image functionality.
    """
    # Mock dependencies
    mock_recognize_objects.return_value = [("n02504458", "tiger", 0.82658235)]
    mock_save_prediction.return_value = "mock_id"

    response = client.post(
        "/process", json={"image_path": "tests/images/tiger_testImage.jpg"}
    )
    assert response.status_code == 200
