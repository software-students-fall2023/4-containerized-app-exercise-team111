import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
from mongomock import MongoClient
from database_manager import DatabaseManager


@pytest.fixture
def mock_db_manager():
    mock_client = MongoClient()
    db_manager = DatabaseManager()
    db_manager.client = mock_client
    return db_manager


def test_save_prediction(mock_db_manager):
    test_data = {
        "image_path": "tests/images/tiger_testImage.jpg",
        "predictions": [{"label": "tiger", "probability": 0.9}],
    }
    result_id = mock_db_manager.save_prediction(
        test_data["image_path"], test_data["predictions"]
    )
    assert result_id is not None


def test_get_results(mock_db_manager):
    mock_db_manager.save_prediction(
        "tests/images/tiger_testImage.jpg", [{"label": "tiger", "probability": 0.9}]
    )
    results = mock_db_manager.get_results()
    assert len(results) > 0
