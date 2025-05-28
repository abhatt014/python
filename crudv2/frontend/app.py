from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import requests


BACKEND_URL = 'http://0.0.0.0:5000'


# --- Flask App Initialization ---
app = Flask(__name__)
app.secret_key = 'your_very_secret_key' # Needed for flash messages, if you add them

# --- Routes ---

# READ: Display all items
@app.route('/')
def index():
    return render_template('login.html')
#register route
@app.route('/register')
def register():
    return render_template('register.html')
#submit route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        requests.post(f'{BACKEND_URL}/submit', json={'username': username, 'password': password})



# --- Run the App ---
if __name__ == '__main__':
    # Make sure to set debug=False in a production environment!
    app.run(host='0.0.0.0', port=4000, debug=True)
