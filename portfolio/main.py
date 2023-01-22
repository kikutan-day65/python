from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/works.html")
def work():
    return render_template("works.html")