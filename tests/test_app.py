from io import BytesIO
import os
from app import app, process_image
import unittest

class TestApp(unittest.TestCase):
    
    def setup_method(self):
        self.app = app.test_client()

    def setUp(self):
        self.app = app.test_client()

    def test_upload_file(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
        response = self.app.post('/upload', data={'file': (BytesIO(image_bytes), 'test_image.jpg')})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'class_label')

    def test_process_image(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
        tags = process_image(image_bytes)
        self.assertEqual(tags, 'Egyptian Cat')
