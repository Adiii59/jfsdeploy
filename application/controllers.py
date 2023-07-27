from flask import current_app as app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html", page = "home")


@app.route("/member/<member>")
def member(member):
    return render_template("index.html", page = "member", member = member)