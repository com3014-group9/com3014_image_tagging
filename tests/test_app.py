import io
import pytest
import os
from app import app

""" @pytest.fixture
def client():
    with app.test_client() as client:
        yield client

#Test case 1 - Positive Upload:
def test_upload_file(client):
    print("Inside test upload func")
    # Test Image path from file system
    with open('/Users/prashdev/Downloads/WallPapers/catsplash.jpeg','rb') as img:
        img_bin = img.read()


 # Make a POST request with the image file
    response = client.post('/upload', data={'file': (io.BytesIO(img_bin), 'catsplash.jpeg')}, content_type='multipart/form-data')

# Check the response
    assert response.status_code == 200
    assert response.data == b'Success'
    print(response)


    # Delete the test file
    os.remove('path/to/test_image.jpg')

 """    

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upload_file(client):
    # Read the test image from the file system
    with open('/Users/prashdev/Downloads/WallPapers/catsplash.jpeg','rb') as f:
        image_bytes = f.read()

    # Make a POST request with the test image
    response = client.post('/upload', data={'file': (io.BytesIO(image_bytes), 'test_image.jpg')},
                           content_type='multipart/form-data')

    # Check the response
    assert response.status_code == 200
    predicted_label = response.get_data(as_text=True).strip().decode()
    #assert predicted_label == 'label'
    print(predicted_label)
