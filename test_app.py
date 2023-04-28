import os
from app import process_image

def test_process_image():
    file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
    with open(file_path, 'rb') as f:
        image_bytes = f.read()
        tags = process_image(image_bytes)
    assert tags == 'Egyptian cat'
