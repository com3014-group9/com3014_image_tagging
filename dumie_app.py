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

"""
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upload_file(client):
    # Read the test image from the file system
    with open('catsplash.jpeg','rb') as f:
        image_bytes = f.read()

    # Make a POST request with the test image
    response = client.post('/upload', data={'file': (io.BytesIO(image_bytes), 'test_image.jpg')},
                           content_type='multipart/form-data')

    # Check the response
    assert response.status_code == 200
    predicted_label = response.get_data(as_text=True).strip()
    assert predicted_label == 'Egyptian cat'
    print(predicted_label)
    """

import pytest
import mongomock
import io
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



""""
import io
from PIL import Image
from app import app
import json

def test_image_processing():
    # Load test image
    test_image = Image.open('catsplash.jpeg')
    # Convert image to bytes
    buffer = io.BytesIO()
    test_image.save(buffer, format='JPEG')
    image_bytes = buffer.getvalue()

    # Send POST request to /upload with test image file
    data = {'file': (io.BytesIO(image_bytes), 'catsplash.jpeg')}
    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2ODMzMTQ1ODksInVzZXJfaWQiOiIwMTIzNDU2Nzg5YWIwMTIzNDU2Nzg5YWIiLCJzY29wZSI6ImFjY2VzcyJ9.S6bx1C1Q34wtgC0ZuG0K391Rw7C0jF17_8M1ZuJmNclStnzlkn7cnsh2PdmPqZeJ_XEzQOfUbo6MvRAdsMLyIqlGqITISy8rbJgwxCIjLkgZ66mamoe6k-2c3wqNxlRHi008bzBmdpQsO-xJXnAeLipNQmDSf_XgMG6iLJ6j4ccAPZo9PAFS04QYucGli3NIzJb4d3--zAhiQre1OkQ51m7HG285SDFCHpAgQcUEj5uFjfs167QfZ_WrywPzZpnv4hz0rK6U4m618XOTq5qe2anZHb4BGAx21e8VdrJgwK-SRh46KKCp2BF8bA0_gGVMmYwFy7epDHsbEfX6aSs-CfiDh3JZmxEYoIlHB6R8io-zGPyHD7b2m4jYmgcEGPHYschuXYYOrOOtbhWRok7_ssQqUz2JNCHvWDe8Fvt9VZNIx67jpW4k-24ChcCbPLHkgw7N8ZxYaYU32-bGpDKB9iOLOdkWHUF0ZN7_QvO6FggJXC6VSUOyzp0RwS2WuRLZ2dZKLy-kAPHSauonQO5wXw69Fac1v9ifRz7iK50g1VuiqMymKwul5HoFPNgJw18F5risjR9AuZEMxzgByG2lIEI2jdF3ujOp8DTC3U7shs2Yuloq56xmIql7Lu3Eva10GR2nqg_-KaZ7NqpDSW36zMAk3pMDliGxhUi8-rm6120'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = app.test_client().post('/upload', data=data, headers=headers, content_type='multipart/form-data')

    # Check if response status code is 200
    assert response.status_code == 200

    # Check if response data is valid JSON
    try:
        json.loads(response.data)
    except ValueError:
        assert False, 'Response data is not valid JSON'

if __name__ == '__main__':
    test_image_processing()
    print('All tests passed!')
"""