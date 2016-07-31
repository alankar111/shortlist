from flask import Flask
from flask import render_template
from flask import request
from models import questions

app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def home():
	question = questions["q1"]
	return render_template('index.html', question=question)
    # return "Hello World!"

@app.route('/<id>')
def next_question(id):
	prev_answers = {}#request.form['prev_answers']
	question = questions[id]

	cur_question = question
	
	while cur_question.nextq is not None:
		cur_question = questions[cur_question.nextq]
		if should_ask_question(cur_question, prev_answers):
			return render_template('index.html', question=cur_question, prev_answers=prev_answers)

	return render_template('results.html')
	

def should_ask_question(id, prev_answers):
	return True