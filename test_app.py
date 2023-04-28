from app import process_image

def test_process_image():
    with open('test_image.jpg', 'rb') as f:
        image_bytes = f.read()

    tags = process_image(image_bytes)
    assert isinstance(tags, str)
