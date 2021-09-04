from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        'name': 'World',
        'age': '42' 
    }
    data = json.dumps(data)

    return data
    