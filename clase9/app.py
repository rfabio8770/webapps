from flask import Flask, render_template, request

# crear una nueva aplicacion web
app = Flask(__name__) 

@app.route("/")
def index():
    # headline = "Hello, World!"
    return render_template("index.html")

@app.route("/otro", methods=["POST"])
def otro():
    parameters = []
    parameters.append(request.form.get("name"))
    parameters.append(request.form.get("ciudad"))
    return render_template("otro.html", parameters=parameters)
