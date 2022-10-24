from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/gerente')
def gerente():
    return render_template('gerente.html')

@app.route('/Administrador')
def administrador():
    return render_template('Administrador.html')

@app.route("/filme")
def filme():
    return ("filme")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/comprarIngresso')
def comprar():
    return render_template('compradeIngresso.html')





# colocar no ar
if (__name__ == "__main__"):
    app.run(debug=True)
