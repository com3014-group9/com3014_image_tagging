from flask import Flask, request
from io import BytesIO
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

from auth_middleware import auth_required

app = Flask(__name__)

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

def process_image(image_bytes):
    image = Image.open(BytesIO(image_bytes))
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]

@app.route('/get_tags', methods=['POST']) #changed /path name
@auth_required
def upload_file(user_id):
    print("MEOW", user_id)
    # Get the file from the POST request
    file = request.files['file']
    print(file)
    image_bytes = file.read()

    tags = process_image(image_bytes)

    # Return a response to the client
    return {"tags" : tags}, 200

if __name__ == '__main__':
    # Start the Flask application with a specified port number
    app.run(port=3304, host = "0.0.0.0")
    