from flask import Flask,request,render_template 
from datetime import datetime 
import requests

BACKEND_URL = 'http://127.0.0.1:9000/'
# --- Flask App Initialization ---
app = Flask(__name__)


# --- Routes ---
@app.route('/')
def index():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html',current_date=current_date)

@app.route('/submit',methods=['POST'])
def submit():
    #submit form data to backend
    form_data = dict(request.form)
    requests.post(BACKEND_URL +'/submit',json=form_data)
    return "data saved Successfully"


if __name__ == '__main__':
    app.run(debug=True)



