from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
from exporter import save_to_file

app = Flask(__name__,template_folder='templates')
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template(
        "report.html"
        ,searchingBy=word
        ,resultsNumber=len(jobs)
        ,jobs = jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower() 
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return f"Generate CSV for {word}"
    except:
        return redirect("/");
    
        

app.run(host="0.0.0.0",port =8081)