from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
import datetime

# --- App Initialization and Configuration ---
app = Flask(__name__)
app.secret_key = 'your_backend_secret_key'
# Allow all origins for simplicity in this non-JS server-to-server context for /api/users
# Login still benefits from stricter CORS if called by JS hypothetically.
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


# --- File Storage Configuration ---
DATA_FILE = 'users.json'

# --- Helper Functions for File I/O (same as before) ---
def load_users():
    if not os.path.exists(DATA_FILE): return []
    try:
        with open(DATA_FILE, 'r') as f: users = json.load(f)
        return users
    except: return []

def save_users(users):
    try:
        with open(DATA_FILE, 'w') as f: json.dump(users, f, indent=4)
    except IOError as e: print(f"Error saving users: {e}")

def get_next_user_id(users):
    if not users: return 1
    return max(user.get('id', 0) for user in users) + 1

# --- API Routes ---

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"error": "Username, password, and email are required"}), 400

    username = data['username']
    password = data['password']
    email = data['email']
    full_name = data.get('full_name', '')
    users = load_users()

    if any(u['username'] == username for u in users) or any(u['email'] == email for u in users):
        return jsonify({"error": "Username or email already exists"}), 409

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user_id = get_next_user_id(users)
    created_at_iso = datetime.datetime.utcnow().isoformat() + "Z"
    
    new_user = {
        "id": new_user_id, "username": username, "password_hash": hashed_password,
        "email": email, "full_name": full_name, "created_at": created_at_iso,
        "created_at_formatted": datetime.datetime.fromisoformat(created_at_iso.replace("Z","")).strftime("%Y-%m-%d %H:%M")
    }
    users.append(new_user)
    save_users(users)
    return jsonify({"message": "User registered successfully", "user_id": new_user_id}), 201

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username']
    password = data['password']
    users = load_users()
    user = next((u for u in users if u['username'] == username), None)

    if user and check_password_hash(user['password_hash'], password):
        session['backend_user_id'] = user['id'] # Backend sets its own session
        session['backend_username'] = user['username']
        return jsonify({"message": "Login successful", "username": user['username'], "user_id": user['id']}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop('backend_user_id', None)
    session.pop('backend_username', None)
    return jsonify({"message": "Backend logout successful"}), 200

@app.route('/api/users', methods=['GET'])
def api_get_users():
    # For this NO-JS server-to-server example, we are simplifying.
    # In a real scenario, this endpoint would be protected by API keys or OAuth2 for server-to-server.
    # We are removing the direct session check here, assuming the frontend server is trusted.
    # if 'backend_user_id' not in session:
    #     return jsonify({"error": "Backend: Unauthorized"}), 401

    users = load_users()
    display_users = []
    for u in users:
        user_data = u.copy()
        user_data.pop('password_hash', None)
        if 'created_at' in user_data and 'created_at_formatted' not in user_data:
             try:
                dt_obj = datetime.datetime.fromisoformat(user_data['created_at'].replace('Z', '+00:00'))
                user_data['created_at_formatted'] = dt_obj.strftime("%Y-%m-%d %H:%M")
             except ValueError:
                user_data['created_at_formatted'] = user_data['created_at']
        display_users.append(user_data)
    return jsonify(sorted(display_users, key=lambda x: x.get('username', '').lower())), 200

# /api/check_auth is less relevant if frontend manages its own session state
# based on login response and doesn't rely on backend cookie for this check via JS.

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE): save_users([])
    app.run(host='0.0.0.0', port=5001, debug=True)
