# coding=utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path
from sqlalchemy import create_engine
from collections import Counter


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

def parse_genre(q):
    a = []
    for u in q:
        for column, value in u.items():
            if value.find('|') == -1:
                a.append(value)
            else:
                a.append(value.split('|', 1)[0])
    return Counter(a)

@app.route('/getGenre')
def getGenre():
    return jsonify(json_list=parse_genre(
        engine.execute("SELECT genres from boxoffice WHERE revenue > 0 AND budget > 0")))

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
