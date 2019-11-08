# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS

import os
print(os.getcwd())

app = Flask(__name__)
CORS(app)

@app.route('/')
def rootPage():
    return jsonify("World")