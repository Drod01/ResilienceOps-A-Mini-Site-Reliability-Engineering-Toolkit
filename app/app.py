from flask import Flask, jsonify, request
import time
import random
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return jsonify({'message': 'ResilienceOps service is running'}), 200

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/slow')
def slow_response():
    time.sleep(random.randint(1, 5))
    return jsonify({'message': 'slow response'}), 200

@app.route('/error')
def error_response():
    return jsonify({'error': 'Simulated failure'}), 500

@app.route('/load')
def cpu_load():
    x = 0
    for _ in range(10**7):
        x += 1
    return jsonify({'message': 'CPU spike completed'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
