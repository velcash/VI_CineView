# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path
from sqlalchemy import create_engine


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

parentPath = Path(__file__).parent.parent
engine = create_engine('sqlite:///' + str(parentPath) + "/cine_view.db")

def parse_query(q):
    d, a = {}, []
    for u in q:
        for column, value in u.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)
    return a

@app.route('/budgetAscending')
def budgetAscending():
    return jsonify(json_list = parse_query(engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY budget ASC LIMIT 10")))

@app.route('/budgetDescending')
def budgetDescending():
    return jsonify(json_list = parse_query(engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY budget DESC LIMIT 10")))

@app.route('/incomeAscending')
def incomeAscending():
    return jsonify(json_list = parse_query(engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY revenue ASC LIMIT 10")))

@app.route('/incomeDescending')
def incomeDescending():
    return jsonify(json_list = parse_query(engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY revenue DESC LIMIT 10")))


@app.route('/')
def rootPage():
    return incomeDescending
