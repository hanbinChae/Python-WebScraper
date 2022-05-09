from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<username>") # @ : decorater = 바로 밑에있는 함수 실행
def contact(username):
    return f"Hello {username} how are you"

app.run(host="0.0.0.0",port =8080)