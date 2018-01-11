from flask import Flask, render_template

from flask_ask import Ask, statement, question, session 

import json, requests, time

from unidecode import unidecode

with open('keys.txt', 'r') as fp:
	credentials = [x.strip() for x in fp.readlines()]

url = ('https://newsapi.org/v2/top-headlines?'
'sources=bbc-news&' + credentials[0])

response=requests.get(url)

app = Flask(__name__)

ask = Ask(app, "/data")

@app.route('/')
def homepage():

	return 'Hello foo bar baz'
	
	
@app.route('/news')
def get_news():

	print response.json()
	
	return render_template('news.html')
	
@ask.intent('HelloIntent')
def hello(firstname):
	text = render_template('hello', firstname=firstname)
	return statement(text).simple_card('Hello', text)
	
		
	
if __name__ == '__main__':
	app.run(debug=True)
	
