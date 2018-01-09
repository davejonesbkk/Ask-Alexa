from flask import Flask

from flask_ask import Ask, statement, question, session 

import json, requests, time, unidecode 



app = Flask(__name__)

ask = Ask(app, "/data")

@app.route('/')
def homepage():

	return 'Hello foo bar baz'
	
	
@app.route('/')
def get_post_titles():

	pass
	
if __name__ == '__main__':
	app.run(debug=True)
	
