import datetime
from flask import Flask, render_template

# crear una nueva aplicacion web
app = Flask(__name__) 

@app.route("/")
def index():
    now = datetime.datetime.now()
    answer = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=answer)