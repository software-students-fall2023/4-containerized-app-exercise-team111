import os
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


import mongomock
import pytest
from io import BytesIO

from app import app as flask_app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "")))


@pytest.fixture
def app():
    """
    Create a fixture for the Flask app.
    """
    yield flask_app


@pytest.fixture
def client(app):
    """
    Create a test client for the Flask app.
    """
    return app.test_client()


def test_index_route(client):
    """
    Test the index route.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.content_type


def test_upload_no_image(client):
    """
    Test uploading without an image.
    """
    response = client.post("/upload", data={})
    assert response.status_code == 400
    assert "No image file provided" in response.json["error"]


def test_upload_empty_filename(client):
    """
    Test uploading with an empty filename.
    """
    data = {"image": (BytesIO(), "")}
    response = client.post("/upload", data=data)
    assert response.status_code == 400
    assert "No selected file" in response.json["error"]


@pytest.fixture
def mock_mongo(monkeypatch):
    """
    Mock the MongoDB client.
    """
    mock_client = mongomock.MongoClient()
    monkeypatch.setattr("pymongo.MongoClient", lambda *args, **kwargs: mock_client)
    return mock_client


def test_mongo_connection(mock_mongo):
    """
    Test MongoDB connection and basic interaction.
    """
    db = mock_mongo["object_recognition_db"]
    collection = db["test_collection"]

    # Insert a document
    collection.insert_one({"test_key": "test_value"})

    # Retrieve the document
    retrieved = collection.find_one({"test_key": "test_value"})

    assert retrieved["test_key"] == "test_value"
