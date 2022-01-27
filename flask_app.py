from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ankita')
def hello():
    return 'Hello, Ankita!'

@app.route('/singh')
def singh():
    return 'Hello, singh!'

app.run(debug=True)