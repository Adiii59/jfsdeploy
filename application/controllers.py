from flask import current_app as app
from flask import render_template
from .data import MEMBERS

@app.route("/")
def home():
    return render_template("index.html", page = "home")


@app.route("/member/<member>")
def member(member):
    member = MEMBERS.get(member, "none")
    return render_template("index.html", page = "member", member = member)
