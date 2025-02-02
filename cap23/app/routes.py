from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { "username": "Ricardo" }
    return render_template("index.html", titulo="Home", user=user)
