from flask import Flask, render_template

# crear una nueva aplicacion web
app = Flask(__name__) 

@app.route("/")
def index():
    # headline = "Hello, World!"
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")
