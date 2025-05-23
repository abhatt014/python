from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

# --- Database Configuration ---
# IMPORTANT: Replace with your actual MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'  # e.g., 'root'
DB_PASSWORD = ''
DB_NAME = 'flask_crud_app'

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
app.secret_key = 'your_very_secret_key' # Needed for flash messages, if you add them

# --- Routes ---

# READ: Display all items
@app.route('/')
def index():
    """Displays all items from the database."""
    conn = get_db_connection()
    if conn is None:
        return "Error: Could not connect to the database.", 500
    
    cursor = conn.cursor(dictionary=True) # dictionary=True to get rows as dictionaries
    try:
        cursor.execute("SELECT id, name, description FROM items ORDER BY created_at DESC")
        items = cursor.fetchall()
    except Error as e:
        print(f"Error fetching items: {e}")
        items = [] # Return empty list on error
    finally:
        cursor.close()
        conn.close()
        
    return render_template('index.html', items=items)

# CREATE: Add a new item
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    """Handles adding a new item to the database."""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name: # Basic validation
            # You might want to use flash messages here for better UX
            return "Error: Name is required.", 400

        conn = get_db_connection()
        if conn is None:
            return "Error: Could not connect to the database.", 500

        cursor = conn.cursor()
        try:
            sql = "INSERT INTO items (name, description) VALUES (%s, %s)"
            val = (name, description)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error adding item: {e}")
            conn.rollback() # Rollback in case of error
            return "Error adding item to database.", 500
        finally:
            cursor.close()
            conn.close()
            
        return redirect(url_for('index')) # Redirect to the main page after adding
    
    # For GET request, just show the add item form
    return render_template('add_item.html')

# UPDATE: Edit an existing item
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    """Handles editing an existing item."""
    conn = get_db_connection()
    if conn is None:
        return "Error: Could not connect to the database.", 500
    
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name:
            return "Error: Name is required.", 400
        
        try:
            sql = "UPDATE items SET name = %s, description = %s WHERE id = %s"
            val = (name, description, item_id)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error updating item: {e}")
            conn.rollback()
            return "Error updating item in database.", 500
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('index'))

    # For GET request, fetch the item and show the edit form
    try:
        cursor.execute("SELECT id, name, description FROM items WHERE id = %s", (item_id,))
        item = cursor.fetchone()
    except Error as e:
        print(f"Error fetching item for edit: {e}")
        item = None
    finally:
        cursor.close()
        conn.close()

    if item is None:
        return "Error: Item not found.", 404
        
    return render_template('edit_item.html', item=item)

# DELETE: Remove an item
@app.route('/delete/<int:item_id>', methods=['POST']) # Use POST for delete for safety
def delete_item(item_id):
    """Handles deleting an item from the database."""
    conn = get_db_connection()
    if conn is None:
        return "Error: Could not connect to the database.", 500
        
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM items WHERE id = %s"
        val = (item_id,)
        cursor.execute(sql, val)
        conn.commit()
    except Error as e:
        print(f"Error deleting item: {e}")
        conn.rollback()
        return "Error deleting item from database.", 500
    finally:
        cursor.close()
        conn.close()
        
    return redirect(url_for('index'))

# --- Run the App ---
if __name__ == '__main__':
    # Make sure to set debug=False in a production environment!
    app.run(debug=True)
