import io
from PIL import Image
from app import app

def test_upload_file():
    with app.test_client() as client:
        # Load an example image for testing
        with open('tests/example_image.jpg', 'rb') as f:
            image_bytes = io.BytesIO(f.read())

        # Send a POST request to the /upload endpoint with the example image
        response = client.post('/upload', data={'file': image_bytes})

        # Check that the response contains the expected tags
        assert b'cat' in response.data
