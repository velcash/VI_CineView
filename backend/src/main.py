# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS

import os
print(os.getcwd())

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')
def rootPage():
    return jsonify("World")
