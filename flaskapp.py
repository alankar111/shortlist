from flask import Flask
from flask import render_template

app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_world():
	return render_template('index.html')
    # return render_template('question.html')
    # return "Hello World!"