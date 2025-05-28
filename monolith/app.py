from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from mysql.connector import Error
#from werkzeug.security import generate_password_hash, check_password_hash
import os # For secret key

# --- App Initialization and Configuration ---
app = Flask(__name__)
# IMPORTANT: Set a strong, random secret key in a real application!
# You can generate one using: import os; os.urandom(24)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_default_very_secret_key_for_dev')

# --- Database Configuration ---
# Replace with your actual MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'  # e.g., 'root'
DB_PASSWORD = '' # Your MySQL password
DB_NAME = 'flask_auth_app'

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
        flash(f"Database connection error: {e}", "danger") # Flash error to user
        return None

# --- Routes ---

@app.route('/')
def index():
    """Redirects to dashboard if logged in, else to login page."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if 'user_id' in session: # If already logged in, redirect to dashboard
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required.', 'warning')
            return render_template('login.html')

        conn = get_db_connection()
        if conn is None:
            # Error already flashed by get_db_connection
            return render_template('login.html')

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, username, password_hash FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user and user['password_hash'] == password:
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Logged in successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.', 'danger')
        except Error as e:
            print(f"Login error: {e}")
            flash('An error occurred during login. Please try again.', 'danger')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Displays the user dashboard with a list of all users."""
    if 'user_id' not in session:
        flash('You need to be logged in to view the dashboard.', 'warning')
        return redirect(url_for('login'))

    conn = get_db_connection()
    if conn is None:
        # Error already flashed by get_db_connection
        # Potentially redirect or show an error page specific to dashboard
        return render_template('dashboard.html', username=session.get('username'), all_users=[], error="Could not fetch user list due to database error.")


    cursor = conn.cursor(dictionary=True)
    all_users_list = []
    try:
        cursor.execute("SELECT id, username, email, full_name, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i') AS created_at_formatted FROM users ORDER BY username")
        all_users_list = cursor.fetchall()
    except Error as e:
        print(f"Error fetching all users for dashboard: {e}")
        flash('Could not retrieve the list of users.', 'danger')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            
    return render_template('dashboard.html', username=session.get('username'), all_users=all_users_list)

@app.route('/logout')
def logout():
    """Logs the user out."""
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# --- Optional: Add a route to register users (for easier testing) ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration (basic example)."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        full_name = request.form.get('full_name')

        if not username or not password or not email:
            flash('Username, password, and email are required.', 'warning')
            return render_template('register.html') # You'd need to create this template

        hashed_password = password
        conn = get_db_connection()
        if conn is None:
            return render_template('register.html')
        
        cursor = conn.cursor()
        try:
            # Check if username or email already exists
            cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
            if cursor.fetchone():
                flash('Username or email already exists.', 'danger')
                return render_template('register.html')

            sql = "INSERT INTO users (username, password_hash, email, full_name) VALUES (%s, %s, %s, %s)"
            val = (username, hashed_password, email, full_name)
            cursor.execute(sql, val)
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Error as e:
            print(f"Registration error: {e}")
            conn.rollback()
            flash(f'An error occurred during registration: {e}', 'danger')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    # For GET request, show registration form
    # You would need to create a templates/register.html file
    #return "Registration page (GET). Create templates/register.html with a form." 
    return render_template('register.html') 


# --- Run the App ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
