from flask import Flask, request
from io import BytesIO
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

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

@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the file from the POST request
    file = request.files['file']
    image_bytes = file.read()

    tags = process_image(image_bytes)

    # Return a response to the client
    return tags

if __name__ == '__main__':
    # Start the Flask application with a specified port number
    app.run(port=5000,host="0.0.0.0")