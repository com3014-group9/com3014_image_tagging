import io
import os
import requests
import unittest

from PIL import Image
from app import app, process_image

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_file(self):
        # Load test image
        img_path = os.path.join(os.getcwd(), "tests", "test_image.jpg")
        with open(img_path, "rb") as f:
            image_bytes = f.read()

        # POST request to upload the test image
        response = self.app.post("/upload", content_type='multipart/form-data',
                                 data={"file": (io.BytesIO(image_bytes), "test_image.jpg")})

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response body is not empty
        self.assertTrue(response.data)

        # Check if the predicted tags match the expected tags
        expected_tags = ["bicycle", "unicycle", "mountain bike", "tricycle"]
        self.assertTrue(all(tag in response.get_data(as_text=True) for tag in expected_tags))
        
    def test_process_image(self):
        # Load test image
        img_path = os.path.join(os.getcwd(), "tests", "test_image.jpg")
        with open(img_path, "rb") as f:
            image_bytes = f.read()

        # Call process_image function and check if the predicted tags match the expected tags
        expected_tags = ["bicycle", "unicycle", "mountain bike", "tricycle"]
        predicted_tags = process_image(image_bytes)
        self.assertTrue(all(tag in predicted_tags for tag in expected_tags))

if __name__ == '__main__':
    unittest.main()
