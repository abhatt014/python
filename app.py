from flask import Flask
import math
# app initialization
app = Flask(__name__)

@app.route('/')
def home():
	
	return 	index_html


@app.route('/welcome')
def welcome():
	return "<h1>HELLO WORLD</h1>"
# route is /api/23
@app.route('/api/<number>')
def show_num(number):
	number = int(number)
	res = math.factorial(number)
	msg = f" the Factorial = {res}"
	return msg


if __name__ == '__main__':
# launch app		
	app.run()