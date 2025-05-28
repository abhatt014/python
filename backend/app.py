from flask import Flask,render_template,request,jsonify
from datetime import datetime as dt
import mysql.connector
app = Flask(__name__)

DB_HOST = 'localhost'
DB_USER = 'root'  # e.g., 'root'
DB_PASSWORD = ''
DB_NAME = 'welcome'

# --- Helper Function to Get Database Connection ---
def get_db_connection():
    """Establishes a connection to the MySQL database."""
    conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    return conn

@app.route('/')
def index():
    return "use /list to view all records"

@app.route('/list', methods=['POST'])
def list():
    if request.method == 'POST':
        formdata  = dict(request.json)
        
        # # connec to mysql , and run query select * from users 
        # conn = get_db_connection()
        # cursor = conn.cursor(dictionary=True)
        # cursor.execute('SELECT * FROM users')
        # users = cursor.fetchall()

        # cursor.close()
        # conn.close()
        return formdata



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)