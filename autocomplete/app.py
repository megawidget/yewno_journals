from time import time
from json import dumps

from flask import Flask, request
from pymongo import MongoClient
from redis import Redis

app = Flask('autocomplete')
journals_db = MongoClient("mongodb://mongo:27017").journals.journals
autocomplete_db = Redis(host='redis', port=6379)

JSON = {'ContentType': 'application/json'}
MINUTE = 60

# routes section
@app.route('/v1/journals/suggest')
def suggest():
    substring = request.args.get('title').lower()
    title = autocomplete_db.get(substring)
    if not title:
        journal = journals_db.find_one({
            'title': { '$regex': '^' + substring, '$options': "-i" }
        })
        if not journal:
            return '', 200, JSON
        title = journal['title']
        autocomplete_db.set(substring, title)
        autocomplete_db.expire(substring, MINUTE)
    return dumps({ 'title': title }), 200, JSON


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
