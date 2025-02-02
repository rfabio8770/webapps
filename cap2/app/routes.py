from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { "username": "Ricardo" }
    return """
    <html>
     <head>
        <title>Segundo Proyecto de Flask - Templates"</title>
    </head>
    <body>
        <h1>Hola, """ + user["username"] + """!</h1>
    </body>
    </html>"""
