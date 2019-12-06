# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path
from sqlalchemy import create_engine


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def rootPage():
    parentPath = Path(__file__).parent.parent
    engine = create_engine('sqlite:///' + str(parentPath) + "/cine_view.db")
    return jsonify(engine.execute("SELECT * from palme"))
