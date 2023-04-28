import os
from io import BytesIO
from PIL import Image
from unittest import TestCase
from app import app, process_image

class TestApp(TestCase):

    def test_process_image(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
            class_label = process_image(image_bytes)
        expected_class_label = 'Egyptian cat'
        self.assertEqual(class_label, expected_class_label)

    def test_upload_file(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
        response = self.client.post('/upload', data={'file': (BytesIO(image_bytes), 'test_image.jpg')})
        expected_response_data = 'Egyptian cat'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), expected_response_data)
