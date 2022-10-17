from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/gerente')
def gerente():
    return render_template("gerente.html")

@app.route('/Administrador')
def administrador():
    return ("ADM")

@app.route('/filme')
def filme():
    return ("gerente")

@app.route('/login')
def login():
    return render_template("login.html")

# colocar no ar
if (__name__ == "__main__"):
    app.run(debug=True)
