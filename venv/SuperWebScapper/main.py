from flask import Flask

app = Flask("SuperWebCrawler")

@app.route("/")
def home():
    return "Hello! Welcome to hanbin's site!"

@app.route("/contact") # @ : decorater = 바로 밑에있는 함수 실행
def contact():
    return "Contact me!"

app.run(host="0.0.0.0",port =8080)