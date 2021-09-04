from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        'name': 'World',
        'age': '42' 
    }
    return data
    