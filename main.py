import flask
import sqlite3
import random

app = flask.Flask(__name__)

#Enable debug mode for now. Disable later once live
app.config['DEBUG'] = True

# Set up database connection
USER_DB_PATH = './users.testing.db'
def getDB() -> sqlite3.Connection:
    db = getattr(flask.g, '_database', None)
    if db is None:
        db = flask.g._database = sqlite3.connect(USER_DB_PATH)
    return db

def sanitize(string: str) -> str:
    dirt = """"*+'#()[]{}\\!?=-_"""
    for i in dirt:
        if i in string:
            string.replace(i, f'\\{i}')
    return string

@app.teardown_appcontext
def close_connection(exception) -> None:
    db = getattr(flask.g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def root():
    message = "Working"
    return flask.render_template('index.html', message=message)

# THIS IS DANGEROUS, REMOVE BEFORE GOING LIVE
@app.route('/readall', methods=['GET'])
def read_all():
    cursor = getDB().cursor()
    data = []
    if 'id' in flask.request.args:
        for i in cursor.execute('SELECT * FROM users WHERE id = ?',flask.request.args['id']):
            temp = {'id':i[0],
                    'name':i[1],
                    'mail':i[2],
                    'pw-hash':i[3]}
            data.append(temp)
    if 'name' in flask.request.args:
        for i in cursor.execute('SELECT * FROM users WHERE name = ?',flask.request.args['name']):
            temp = {'id':i[0],
                    'name':i[1],
                    'mail':i[2],
                    'pw-hash':i[3]}
            data.append(temp)
    if 'mail' in flask.request.args:
        for i in cursor.execute('SELECT * FROM users WHERE mail = ?',flask.request.args['mail']):
            temp = {'id':i[0],
                    'name':i[1],
                    'mail':i[2],
                    'pw-hash':i[3]}
            data.append(temp)
    if 'pw' in flask.request.args:
        for i in cursor.execute('SELECT * FROM users WHERE pw = ?',flask.request.args['pw']):
            temp = {'id':i[0],
                    'name':i[1],
                    'mail':i[2],
                    'pw-hash':i[3]}
            data.append(temp)
    #if 'name' and 'mail' and 'id' and 'pw-hash' not in flask.request.args:
    #    for i in cursor.execute('SELECT * FROM users;').fetchall():
    #        temp = {'id':i[0],
    #                'name':i[1],
    #                'mail':i[2],
    #                'pw-hash':i[3]}
    #        data.append(temp)
    if len(data) > 0:
        return flask.jsonify(data)
    else:
        return "no matches found"

# Experimenting with transmitting data to the server
"""
Headers (-H in curl) are available to read as a tupple in flask.request.headers. The specifics are [(key, value),(key2, value2)]
the data is just strings
"""
@app.route('/api/alpha/set/newsub', methods=['GET'])
def newsub():
    data = set(flask.request.headers)
    usefulData = []
    for i in data:
        if i[0] == "id" or "lvl":
            usefulData.append(i)
    if len(USER_DB_PATH) != 2:
        flask.abort(400)

@app.route('/api/alpha/get/bannedWords', methods=['GET'])
def getBannedWords():
    with open("banned.txt") as handler:
        data = handler.readlines()
        for i in data:
            key = data.index(i)
            if '\n' in i:
                print("yes")
                i = i[:-1]
                data[key] = i
        return flask.jsonify(data)
