from flask import Flask,render_template,request
from datetime import datetime as dt
import requests
BACKEND_URL = 'http://127.0.0.1:9000'
app = Flask(__name__)

@app.route('/')
def index():
    current_date = dt.now()
    return render_template('index.html',current_date=current_date)

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        formdata = dict(request.form)
      
        #submit route
    response = requests.post(f'{BACKEND_URL}/list', json=formdata)
    return str(response)



if __name__ == '__main__':
    app.run(debug=True)