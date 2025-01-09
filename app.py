from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fonction pour effectuer les calculs
def calculer(operation, a=None, b=None):
    try:
        a = float(a) if a else None
        b = float(b) if b else None
        if operation == "addition":
            return a + b
        elif operation == "soustraction":
            return a - b
        elif operation == "multiplication":
            return a * b
        elif operation == "division":
            return a / b if b != 0 else "Erreur : Division par zéro"
        elif operation == "puissance":
            return a ** b
        elif operation == "racine":
            return math.sqrt(a)
        elif operation == "logarithme":
            return math.log(a)
        elif operation == "sinus":
            return math.sin(math.radians(a))
        elif operation == "cosinus":
            return math.cos(math.radians(a))
        elif operation == "tangente":
            return math.tan(math.radians(a))
    except Exception as e:
        return f"Erreur : {e}"

# Route pour la page principale
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        operation = request.form.get("operation")
        a = request.form.get("a")
        b = request.form.get("b")
        result = calculer(operation, a, b)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)