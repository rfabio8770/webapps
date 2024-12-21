from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora_mayor_edad():
    msg = None
    mensaje = ""
    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            msg= edad < 18
            if edad < 18:
                mensaje = "Eres menor de edad"
            else:
                mensaje ="Eres mayor de edad"
        except ValueError:
            message = "Entrada no válida. Ingrese solo número entero"
    return render_template("index.html", msg=msg, mensaje=mensaje)

