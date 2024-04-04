from flask import Flask, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = 'http://backend:5000'


@app.route('/')
def index():
    return 'Welcome to the frontend!'


@app.route('/get_message')
def get_message():
    response = requests.get(f'{BACKEND_URL}/api/message')
    message = response.json()['message']
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
