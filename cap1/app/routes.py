from app import app

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hola, Ricardo</h1>"
