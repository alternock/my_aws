from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hola Mundo!", "status": "ok"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello!", "status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
