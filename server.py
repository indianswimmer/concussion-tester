import os
import time
import threading

from flask import Flask, jsonify
from flask_cors import CORS

from python_example import main


app = Flask(__name__)
CORS(app)


@app.route('/send_data', methods=['POST'])
def login():
    main()

    while True:
        from python_example import STATE
        if STATE is not None:
            return jsonify({'result': str(STATE)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT')))