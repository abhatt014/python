# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources.
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def home():
    # HTML content for a simple login page
    # In a real application, you would typically use render_template to serve an HTML file.
    # For simplicity here, we are embedding HTML as a multi-line string.
    login_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f2f5;
            }
            .login-container {
                background-color: #fff;
                padding: 20px 40px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            .login-container h2 {
                margin-bottom: 20px;
                color: #333;
            }
            .login-container input[type="text"],
            .login-container input[type="password"] {
                width: calc(100% - 22px);
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
                box-sizing: border-box;
            }
            .login-container input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .login-container input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>Login</h2>
            <form action="/login" method="post">
                <div>
                    <input type="text" name="username" placeholder="Username" required>
                </div>
                <div>
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <div>
                    <input type="submit" value="Login">
                </div>
            </form>
        </div>
    </body>
    </html>
    """
    return login_html

# This block ensures the server only runs when the script is executed directly
# (not when it's imported as a module into another script).
if __name__ == '__main__':
    # app.run() starts the built-in development server.
    # debug=True is very useful during development because:
    #   - The server will automatically reload if you change your code.
    #   - It provides a helpful debugger in the browser if an error occurs.
    # IMPORTANT: Do NOT use debug=True in a production environment!
    app.run(debug=True)
