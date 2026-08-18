from flask import Flask, render_template, request, url_for, redirect

# Importa o SQLAlchemy para trabalhar com banco de dados
from flask_sqlalchemy import SQLAlchemy

# Cria a aplicação Flask
app = Flask(__name__)


# Define o banco SQLite que será utilizado
# O arquivo "banco.db" será criado automaticamente
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

# Desativa o rastreamento de alterações do SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conecta o SQLAlchemy à aplicação Flask
db = SQLAlchemy(app)


# ============================================================
# MODEL / TABELA USUARIO
# ============================================================

# Cria uma tabela chamada "usuario"
class Usuario(db.Model):

    # ID do usuário
    # primary_key=True = chave primária
    id = db.Column(db.Integer, primary_key=True)

    # Nome de usuário
    # unique=True = não permite usuários repetidos
    # nullable=False = campo obrigatório
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    # Senha do usuário
    # nullable=False = campo obrigatório
    senha = db.Column(
        db.String(80),
        nullable=False
    )


# ============================================================
# CRIAÇÃO DO BANCO
# ============================================================

# Cria as tabelas no banco caso elas ainda não existam
with app.app_context():
    db.create_all()

if __name__ == "__main__":

    # Inicia o servidor Flask
    #
    # debug=True:
    # - Mostra erros detalhados
    # - Reinicia automaticamente quando o código muda
    app.run(debug=True)