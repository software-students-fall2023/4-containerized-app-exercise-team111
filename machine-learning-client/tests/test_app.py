import pytest
import sys
import os
import numpy as np


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app
from unittest.mock import patch, MagicMock


@pytest.fixture
def client():
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
    mock_cv2_imread,
    mock_os_path_exists,
    mock_save_prediction,
    mock_recognize_objects,
    client,
):
    # Mock dependencies
    mock_recognize_objects.return_value = [("n02504458", "tiger", 0.82658235)]
    mock_save_prediction.return_value = "mock_id"

    response = client.post(
        "/process", json={"image_path": "tests/images/tiger_testImage.jpg"}
    )
    assert response.status_code == 200
