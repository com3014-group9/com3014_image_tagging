import unittest
from io import BytesIO
from app import app, process_image

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_upload_file(self):
        with open('test_image.jpg', 'rb') as f:
            image_bytes = f.read()
        response = self.client.post('/upload', data={'file': (BytesIO(image_bytes), 'test_image.jpg')})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'class_label')

    def test_process_image(self):
        with open('test_image.jpg', 'rb') as f:
            image_bytes = f.read()
        class_label = process_image(image_bytes)
        self.assertEqual(class_label, 'expected_class_label')

if __name__ == '__main__':
    unittest.main()
