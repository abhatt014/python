from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)

# define routes
# get method
@app.route('/')
def index():
    return 'NOT A VALID PATH!!'

#show login page
@app.route('/login')
def login():
    return render_template('login.html')

#process form data submitted by user
@app.route('/submit', methods=['GET'])
def submit():
    err = "Either username or pasword is not correct!!"
    email = request.args.get('email')
    pwd = request.args.get('password')
    if email == 'demo@example.com':
        if pwd == '123456':
            return render_template('dashboard.html',email=email)
        else:
            return render_template('login.html',err=err)
    else:
        return render_template('login.html',err=err)
    
        

#dashboard route
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

#register route
@app.route('/register')
def register():
    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)