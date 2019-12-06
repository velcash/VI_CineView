# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from pathlib import Path


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def rootPage():
    parentPath = Path(__file__).parent.parent.parent
    myData = pd.read_csv(str(parentPath) + "/Data/Oscars.csv", delimiter=';')
    print(myData)
    return jsonify(list(myData))
