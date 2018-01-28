import os
import time
import threading

from flask import Flask, jsonify
from flask_cors import CORS

from test import *


app = Flask(__name__)
CORS(app)


@app.route('/send_data', methods=['POST'])
def login():
    collectData()

    while True:
        from test import STATE
        if STATE is not None:
            return jsonify({'result': str(STATE)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
