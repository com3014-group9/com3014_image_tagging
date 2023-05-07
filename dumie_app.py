import io
import os
from app import app
import pytest
import mongomock
from unittest.mock import patch
import requests
from PIL import Image
from io import BytesIO
import app
from helpers import generate_access_token

@pytest.fixture()
def client():
    return app.app.test_client()

@pytest.fixture()
def access_header():
    return {'Authorization': f"Bearer {generate_access_token(111)}"}

# Test function to test image processing
def test_image_processing(client, access_header):
    # Load test image
    test_image = Image.open('catsplash.jpeg')
    # Convert image to bytes
    buffer = BytesIO()
    test_image.save(buffer, format='JPEG')
    image_bytes = buffer.getvalue()

    # Send POST request to /get_tags with test image file
    data = {'file': (io.BytesIO(image_bytes), 'catsplash.jpeg')}
    response = client.post('/get_tags', data=data, headers=access_header, content_type='multipart/form-data')

    # Check if response status code is 200
    assert response.status_code == 200

    # Check if the response is not empty
    assert response.data != b''

    print(response.data)
    # Check if the returned value is a string
    #assert isinstance(response.json, str)
