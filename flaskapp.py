from flask import Flask
from flask import render_template
from flask import request
from models import questions
import json

app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def home():
	qid = "q1"
	question = questions[qid]

	return render_template('index.html', question=question, qid=qid, prev_answers=json.dumps({}))

@app.route('/<id>', methods=['POST'])
def next_question(id):
	prev_answers = json.loads(request.form['prev_answers'])
	print id
	question = questions[id]

	# Fetch answers #
	answer = None
	if question.qtype == "picker":
		answer = request.form["amount"]
	elif question.qtype == "single":
		answer = request.form["optionsRadios"]
	else:
		answer = []
		for option in question.getOptions():
			if option in request.form:
				answer.append(request.form[option])

	prev_answers[id] = answer
	# Completed fetching answer #

	cur_question = question
	
	while cur_question.nextq is not None:
		qid = cur_question.nextq
		cur_question = questions[cur_question.nextq]
		if should_ask_question(cur_question, prev_answers):
			return render_template('index.html', question=cur_question, qid=qid, prev_answers=json.dumps(prev_answers))

	return render_template('results.html')
	
def should_ask_question(id, prev_answers):
	return True