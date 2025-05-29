from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests # For making HTTP requests to the backend
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FRONTEND_SECRET_KEY', 'your_frontend_secret_key_for_dev_nojs_docker')

# Configuration for the Backend API URL
# Get this from an environment variable set by Docker Compose
BACKEND_API_BASE_URL = os.environ.get("BACKEND_API_URL", "http://localhost:5001/api") # Default for local non-docker run

@app.route('/')
def index():
    if 'frontend_username' in session:
        return redirect(url_for('dashboard_page'))
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if 'frontend_username' in session:
        return redirect(url_for('dashboard_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required.', 'warning')
            return render_template('login.html', backend_api_url_for_js=BACKEND_API_BASE_URL) # Pass for JS if any (though not primary here)

        try:
            api_response = requests.post(f"{BACKEND_API_BASE_URL}/login", 
                                         json={"username": username, "password": password})
            
            if api_response.status_code == 200:
                user_data = api_response.json()
                session['frontend_username'] = user_data.get('username')
                session['frontend_user_id'] = user_data.get('user_id')
                flash('Logged in successfully!', 'success')
                return redirect(url_for('dashboard_page'))
            else:
                error_data = api_response.json()
                flash(error_data.get('error', 'Invalid username or password.'), 'danger')
        except requests.exceptions.RequestException as e:
            print(f"Error calling backend login API: {e}")
            flash('Could not connect to login service. Please try again later.', 'danger')
        
    return render_template('login.html', backend_api_url_for_js=BACKEND_API_BASE_URL)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if 'frontend_username' in session:
        return redirect(url_for('dashboard_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        full_name = request.form.get('full_name')

        if not username or not password or not email:
            flash('Username, password, and email are required.', 'warning')
            return render_template('register.html', backend_api_url_for_js=BACKEND_API_BASE_URL)

        payload = {
            "username": username, "password": password,
            "email": email, "full_name": full_name
        }
        try:
            api_response = requests.post(f"{BACKEND_API_BASE_URL}/register", json=payload)
            response_data = api_response.json()

            if api_response.status_code == 201:
                flash(response_data.get('message', 'Registration successful! Please login.'), 'success')
                return redirect(url_for('login_page'))
            else:
                flash(response_data.get('error', 'Registration failed.'), 'danger')
        except requests.exceptions.RequestException as e:
            print(f"Error calling backend register API: {e}")
            flash('Could not connect to registration service.', 'danger')
            
    return render_template('register.html', backend_api_url_for_js=BACKEND_API_BASE_URL)


@app.route('/dashboard')
def dashboard_page():
    if 'frontend_username' not in session:
        flash('You need to be logged in to view the dashboard.', 'warning')
        return redirect(url_for('login_page'))

    all_users_list = []
    error_message = None
    try:
        api_response = requests.get(f"{BACKEND_API_BASE_URL}/users") # No auth headers needed for this simplified backend
        
        if api_response.status_code == 200:
            all_users_list = api_response.json()
        else:
            error_data = api_response.json()
            error_message = error_data.get('error', 'Failed to load users from backend.')
            flash(error_message, 'danger')
            
    except requests.exceptions.RequestException as e:
        print(f"Error calling backend users API: {e}")
        error_message = "Could not connect to user service to fetch list."
        flash(error_message, 'danger')

    return render_template('dashboard.html', 
                           username=session.get('frontend_username'), 
                           all_users=all_users_list,
                           error=error_message)

@app.route('/logout')
def logout():
    frontend_username = session.get('frontend_username')
    session.pop('frontend_username', None)
    session.pop('frontend_user_id', None)
    
    try:
        requests.post(f"{BACKEND_API_BASE_URL}/logout") 
    except requests.exceptions.RequestException as e:
        print(f"Note: Could not reach backend logout: {e}")

    flash(f'User {frontend_username if frontend_username else ""} logged out successfully.', 'info')
    return redirect(url_for('login_page'))


if __name__ == '__main__':
    # app.run() will be called by CMD in Dockerfile, which respects FLASK_RUN_HOST/PORT
    # For local running (python app.py), specify host and port:
    app.run(host='0.0.0.0', port=5000, debug=True)
