# Importa flask, Render template, funçao G
from flask import Flask, render_template, g
# Importa SQLITE
import sqlite3

# Cria app
app = Flask("Hello")

DATABASE = "banco.bd"
SECRET_KEY = "chave"

# Faz configuração
app = Flask("Hello")
app.config.from_object(__name__)

# Função para conetar banco
def conecta_bd():
    return sqlite3.connect(DATABASE)

# Função antes da requisição guarda conexão
@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

# Função fecha conexão do banco / (e) para tratamento de erro - exception
@app.teardown_request
def depois_requisicao(e):
    g.bd.close()


# Cria rota + URL + variavel = View do Flask
@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("layout.html", entradas = entradas)