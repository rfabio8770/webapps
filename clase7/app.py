from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sumas():
    msg = None
    mensajes= []
    if request.method == "POST":
        try:
            n = int(request.form["n"])
            msg = n > 0
            if msg:
               sumas = [0] * 3
               for i in range(1,n+1):
                    sumas[0] += i
                    sumas[1] += i ** 2
                    sumas[2] += i ** 3
               mensajes.append(f"Suma de los primeros {n} números naturales es {sumas[0]}\n")
               mensajes.append(f"Suma de los cuadrados de los primeros {n} números naturales es {sumas[1]}\n")
               mensajes.append(f"Suma de los cubos de los primeros {n} números naturales es {sumas[2]}\n")
            else:
               mensajes.append("Error.")
        except ValueError:
            mensajes.append("Error: debe ingresar un numero entero positivo.")
    return render_template("index.html", msg=msg, mensajes= mensajes)

