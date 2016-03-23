from time import time
from json import dumps

from flask import Flask, request
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask('journals')
journals_db = MongoClient("mongodb://mongo:27017").journals.journals

JSON = {'ContentType': 'application/json'}

# routes section
@app.route('/v1/journals', methods=['GET', 'POST'])
def journals():
    if request.method == 'GET':
        return get_journals()
    return create_journal()

@app.route('/v1/journals/<journal_id>', methods=['GET', 'POST', 'DELETE'])
def journals_with_id(journal_id):
    if request.method == 'GET':
        return get_journals(journal_id)
    if request.method == 'POST':
        return update_journal(journal_id)
    return delete_journal(journal_id)

# actual operations on journals
def get_journals(journal_id=None):
    cursor = journals_db.find({ '_id': ObjectId(journal_id) } if journal_id else None)
    results = []
    for item in cursor:
        results.append({
            'journal_id': str(item['_id']),
            'title': item['title'],
            'created': item['created'],
            'updated': item['updated'],
        })
    return dumps(results), 200,  JSON

def create_journal():
    title = request.form['title']
    assert title
    now = time()
    journals_db.insert_one({ 'title': title, 'created': now, 'updated': now })
    return '', 200, JSON

def update_journal(journal_id):
    title = request.form['title']
    assert title
    now = time()
    journals_db.update_one(
        { '_id': ObjectId(journal_id) },
        { "$set": { 'title': title, 'updated': now } }
    )
    return '', 200, JSON

def delete_journal(journal_id):
    journals_db.delete_many({ '_id': ObjectId(journal_id) })
    return '', 200, JSON


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
