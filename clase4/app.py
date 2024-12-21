from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def imc_calculator():
    imc = None
    message = ""
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            imc = round(peso / (altura ** 2), 2)
            
            if imc < 18.5:
                message = "Usted está bajo de peso."
            elif 18.5 <= imc < 24.9:
                message = "Usted tiene un peso normal."
            elif 25 <= imc < 29.9:
                message = "Usted tiene sobrepeso."
            else:
                message = "Usted está obeso."
        except ValueError:
            message = "Entrada no válida. Ingrese solo números"
    return render_template("index.html", imc=imc, message=message)

