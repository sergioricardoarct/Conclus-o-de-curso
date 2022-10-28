from app import db


class Clientes(db.Model):
    __tablename__ = 'CLIENTES'

    id = db.Column(db.integer, primary_key=True)
    nomeUser = db.Column(db.String, unique=True)
    CPF = db.Column(db.integer)
    nome = db.Column(db.String)
    senha = db.Column(db.String)
    telefone = db.Column(db.integer)
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

    id = db.Column(db.integer, primary_key=True)
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

