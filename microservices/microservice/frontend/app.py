from flask import Flask,request,render_template 
from datetime import datetime 
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

# --- Routes ---
@app.route('/')
def index():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html',current_date=current_date)

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        username  = request.form['username']
        password = request.form['password']
        #insert username and password in user table
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO users (username,password) VALUES (%s,%s)"
        val = (username,password)
        cursor.execute(sql,val)
        conn.commit()
        cursor.close()
        conn.close()
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
    app.run(debug=True)



