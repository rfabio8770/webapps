from flask import Flask

app = Flask(__name__) # crear una nueva aplicacion web

@app.route("/")
def index():
    return "Hola, mundo!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hola {name} </h1>"
