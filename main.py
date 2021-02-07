# This will be the main server for general purpose activities of the bots, 
# like checking against banned phrases, sharing data, etc

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

some_data = [
    {
        "value1": "key1",
        "value2": "key2",
        "id": 0
    }, 
    {
        "value3": "value3",
        "value4": "value4",
        "id": 1
    }
]

@app.errorhandler(404)
def page_not_found():
    return '<h1>ERROR 404</h1><p>The resource could not be found.</p>'

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/data', methods=['GET'])
def data_all():
    return flask.jsonify(some_data)

@app.route('/data/id', methods=['GET'])
def specific_data():
    if 'id' in flask.request.args:
        try:
            id = int(flask.request.args['id'])
        except ValueError:
            return 'ERROR: Value "id" must be an integer'
    else:
        return 'ERROR: Value "id" must be set'
    
    results = []

    for i in some_data:
        if i['id'] == id:
            results.append(i)
    
    return flask.jsonify(results)

if "__name__" == "__main__":
    app.run()