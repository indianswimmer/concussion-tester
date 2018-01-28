import os
import time

from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint


app = Flask(__name__)
CORS(app)


@app.route('/send_data', methods=['POST'])
def login():
    time.sleep(4)
    # data = request.get_json()
    return jsonify({'pct_chance': str(randint(0, 100))})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT')))
