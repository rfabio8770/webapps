from flask import Flask, render_template

app = Flask(__name__) # crear una nueva aplicacion web

@app.route("/")
def index():
    headline = "Hello, World!"
    return render_template("index.html", headline=headline)

