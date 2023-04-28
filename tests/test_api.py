import io
import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_image(client):
    # Open the test image file
    with open('test_image.jpg', 'rb') as f:
        image_bytes = f.read()

    # Send a POST request to the API endpoint with the image file
    response = client.post('/upload', data={'file': (io.BytesIO(image_bytes), 'test_image.jpg')})

    # Check that the response has a 200 OK status code
    assert response.status_code == 200

    # Check that the response contains the expected tags
    tags = json.loads(response.data)
    assert 'dog' in tags
    assert 'animal' in tags
