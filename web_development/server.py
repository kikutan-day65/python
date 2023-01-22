from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return "this is my blog"

@app.route("/blog/2023/dogs")
def blog2():
    return "this is my dog"