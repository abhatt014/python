from flask import Flask,request
import mysql.connector
from mysql.connector import Error

# --- Database Configuration ---
# IMPORTANT: Replace with your actual MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'  # e.g., 'root'
DB_PASSWORD = ''
DB_NAME = 'monolith_db'

# --- Helper Function to Get Database Connection ---
def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# --- Flask App Initialization ---
app = Flask(__name__)
##app.secret_key = 'your_very_secret_key' # Needed for flash messages, if you add them



@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        username  = request.json['username']
        password = request.json['password']
        #insert username and password in user table
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO users (username,password) VALUES (%s,%s)"
        val = (username,password)
        cursor.execute(sql,val)
        conn.commit()
        cursor.close()
        conn.close()
        return "data submited successfully"
@app.route('/view')
def view():        
        #select * from users and return data
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        form_data = cursor.fetchall()
        cursor.close()
        conn.close()

        #form_data = dict(request.form)
        return form_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)



