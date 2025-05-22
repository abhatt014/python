from flask import Flask , request , jsonify , render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/submit", methods=['POST'])
def submit():
        return request.form.get("username")

  


@app.route("/")
def home():
    current_day = datetime.now().strftime("%A")
    topic = 'devops'
    #Wednesday
    return render_template("index.html", current_day=current_day, topic=topic)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")



# ROUTE FOR /api/data
@app.route("/api/data")
def api_data():
    user = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '123-456-7890'
    }
    return user
   
    # name = request.args.get("name")
    # age = request.args.get("age")
    # response_data = {}
    # response_data["name"] = name
    # response_data["age"] = age
    # return response_data


if __name__ == "__main__":
    app.run(debug=True)