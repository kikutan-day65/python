from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/works.html")
# def work():
#     return render_template("works.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")