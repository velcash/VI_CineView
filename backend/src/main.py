# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
from sqlalchemy import create_engine
from collections import Counter
import sys


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

@app.route('/getFilterByRec',  methods=['POST'])
def getFilterByRec():
    content = request.json
    print(content, file=sys.stderr)
    print(content['type'], file=sys.stderr)
    print(content['palme'], file=sys.stderr)
    print(content['oscar'], file=sys.stderr)
    if content['type'] == 'id':
        return queryIncomingDescending(prepareFilter(content['palme'], content['oscar']))
    else:
        if content['type'] == 'ia':
            return queryIncomingAscending(prepareFilter(content['palme'], content['oscar']))
        else:
            if content['type'] == 'bd':
                return queryBudgetDescending(prepareFilter(content['palme'], content['oscar']))
            else:
                return queryBudgetAscending(prepareFilter(content['palme'], content['oscar']))

def queryBudgetAscending(filter):
    if len(filter) > 0:
        return jsonify(json_list=parse_query(
        engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 AND ({}) ORDER BY budget ASC LIMIT 10".format(filter))))
    else:
        return jsonify(json_list=parse_query(engine.execute("SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY budget ASC LIMIT 10")))

def queryBudgetDescending(filter):
    if len(filter) > 0:
        return jsonify(json_list=parse_query(engine.execute(
        "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 AND ({}) ORDER BY budget DESC LIMIT 10".format(
            filter))))
    else:
        return jsonify(json_list=parse_query(engine.execute(
            "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY budget DESC LIMIT 10")))

def queryIncomingAscending(filter):
    if len(filter) > 0:
        return jsonify(json_list=parse_query(engine.execute(
        "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 AND ({}) ORDER BY revenue ASC LIMIT 10".format(
            filter))))
    else:
        return jsonify(json_list=parse_query(engine.execute(
            "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY revenue ASC LIMIT 10")))

def queryIncomingDescending(filter):
    if len(filter) > 0:
        return jsonify(json_list=parse_query(engine.execute(
        "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 AND ({}) ORDER BY revenue DESC LIMIT 10".format(
            filter))))
    else:
        return jsonify(json_list=parse_query(engine.execute(
            "SELECT * from boxoffice WHERE revenue > 0 AND budget > 0 ORDER BY revenue DESC LIMIT 10")))

def prepareFilter(palme, oscar):
    query = ''
    if oscar == True:
        query += 'boxOffice = 1.0'
    if palme == True:
        if len(query) == 0:
            query += 'palme = 1.0'
        else:
            query += ' OR palme = 1.0'
    return query


@app.route('/budgetAscending',  methods=['POST'])
def budgetAscending():
    content = request.json
    return queryBudgetAscending(prepareFilter(content['palme'], content['oscar']))

@app.route('/budgetDescending',  methods=['POST'])
def budgetDescending():
    content = request.json
    return queryBudgetDescending(prepareFilter(content['palme'], content['oscar']))

@app.route('/incomeAscending',  methods=['POST'])
def incomeAscending():
    content = request.json
    return queryIncomingAscending(prepareFilter(content['palme'], content['oscar']))

@app.route('/incomeDescending',  methods=['POST'])
def incomeDescending():
    content = request.json
    return queryIncomingDescending(prepareFilter(content['palme'], content['oscar']))

@app.route('/')
def rootPage():
    return queryIncomingDescending(prepareFilter(False, False))
