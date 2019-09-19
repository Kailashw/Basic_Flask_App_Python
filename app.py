from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Azure!</h1>'

@app.route('/hi')
def hi():
    return '<h1>Hello, CloudThing!</h1>'