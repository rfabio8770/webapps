from flask import Flask, render_template, request

# crear una nueva aplicacion web
app = Flask(__name__) 

@app.route("/")
def index():
    # headline = "Hello, World!"
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
