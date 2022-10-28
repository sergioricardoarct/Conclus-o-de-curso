#__criação do Projeto para Tcc em análise e desenvilvimento de sistemas__#

#__Importações gerais__#
from flask import Flask, render_template, Response, request
from flask_sqlalchemy import SQLAlchemy

# incialiazação geral #
app = Flask(__name__)


# Banco de dados#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


#__Entidades
class Clientes(db.Model):
    __tablename__ = 'CLIENTES'

    _id = db.Column(db.Integer, primary_key=True)
    nomeUser = db.Column(db.String, unique=True)
    CPF = db.Column(db.Integer)
    nome = db.Column(db.String)
    senha = db.Column(db.String)
    telefone = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)

    def __init__(self, nomeUser, CPF, nome, senha, telefone, email):
        self.nomeUser = nomeUser
        self.CPF = CPF
        self.nome = nome
        self.senha = senha
        self.telefone = telefone
        self.email = email

    def __repr__(self):
        return "<Cliente %r>" %self.nome

class Filmes(db.Model):
    __tablename__ = 'FILMES'

    idFilme = db.Column(db.Integer, primary_key=True)
    nomeFilme = db.Column(db.String, unique=True)
    duracao = db.Column(db.String)
    faixaEtaria = db.Column(db.String)
    descricao = db.Column(db.String)

    def __init__(self, nomeFilme, duracao, faixaEtaria, descricao):

        self.nomeFilme = nomeFilme
        self.duracao = duracao
        self.faixaEtaria = faixaEtaria
        self.descricao = descricao

    def __repr__(self):
        return "<Filme %r>" %self.nomeFilme




# Rotas e paginas#
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/gerente')
def gerente():
    return render_template('gerente.html')

@app.route('/Administrador')
def administrador():
    return render_template('Administrador.html')

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/comprarIngresso')
def comprar():
    return render_template('compradeIngresso.html')



#__colocar no ar__# #depois tirar o debug antes de enviar para a finalização#
if (__name__ == "__main__"):
    app.run(debug=True)
