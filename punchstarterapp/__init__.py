from flask import Flask
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)
@app.route("/")
def hello():
    return "Hello World"
