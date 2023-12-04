import os
import sys
import pytest
from io import BytesIO

from app import app as flask_app  
from requests_mock import Mocker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



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


def test_upload_image(client, requests_mock):
    """
    Test successful image upload.
    """

    # Mock the external request to ML_CLIENT_URL
    requests_mock.post("http://localhost:5003/process", json={"result": "success"})

    # Simulate an image upload
    data = {"image": (BytesIO(b"fake image data"), "tiger_testImage.jpg")}
    response = client.post("/upload", data=data)
    assert response.status_code == 200
    assert response.json == {"result": "success"}
