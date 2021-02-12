import flask
import sqlite3

app = flask.Flask(__name__)

#Enable debug mode for now. Disable later once live
app.config['DEBUG'] = True

# Set up database connection
db_connector = sqlite3.connect("data.db")
db_cursor = db_connector.cursor()

@app.route('/', methods=['GET'])
def main_page():
    a = "placeholder"
    return a