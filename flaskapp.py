from flask import Flask
from flask import render_template

app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def home():
	return render_template('index.html')
    # return "Hello World!"

@app.route('/<id>')
def next_question(id):
	prev_answers = request.form['prev_answers']
	return render_template('index.html', question=question, prev_answers=prev_answers)

def should_ask_question(id, prev_answers):
	return True