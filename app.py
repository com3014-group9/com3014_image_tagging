from flask import Flask,render_template
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests


app = Flask(__name__)

#@app.route('/', methods = ['GET'])
#def x():
#  return render_template('index.html')



@app.route('/')
def hello_world():
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
    url = 'https://wallpaperaccess.com/full/275902.jpg'
    image = Image.open(requests.get(url, stream=True).raw)
    inputs = processor(images=image, return_tensors="pt")
    #inputs = processor(images="https://wallpaperaccess.com/full/275902.jpg", return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return "Predicted class:"+( model.config.id2label[predicted_class_idx])
    #return 'Hello, World!'


#@app.route('/',methods = ['GET'])
#def predict():
#    inputs = processor(images="https://wallpaperaccess.com/full/275902.jpg", return_tensors="pt")
#    outputs = model(**inputs)
#    logits = outputs.logits
#    predicted_class_idx = logits.argmax(-1).item()
#    print("Predicted class:", model.config.id2label[predicted_class_idx])
#    return "dasdasd"


if __name__ == '__main__':

    
    app.run(port =3000,debug = True  )
    
    #processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    #ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
    
