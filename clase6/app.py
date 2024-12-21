from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora_mayor_edad():
    msg = None
    mensaje = ""
    if request.method == "POST":
        try:
            monto = int(request.form["monto"])
            msg = monto > 0
            if msg:
                if monto == 20000:
                    cbilletes = 1
                else:
                    cbilletes = (monto // 20000) 
                    if (monto % 20000 != 0):
                        cbilletes += 1
                mensaje = f"Se necesitan {cbilletes} billetes de G 20000"
            else:
                mensaje ="Error en la entrada. El número debe ser positivo"
        except ValueError:
            message = "Entrada no válida. Ingrese solo número entero"
    return render_template("index.html", msg=msg, mensaje=mensaje)

