from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def x():
    return render_template('index.html')


@app.route('/',methods = ['POST'])
def predict():
    return "dasdasd"


if __name__ == '__main__':
    app.run(port =3000,debug = True  )