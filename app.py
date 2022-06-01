# Importa flask, Render template, funçao G
from flask import Flask, render_template, g, request, flash, session, redirect, url_for, abort
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
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC;"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("exibir_entradas.html", entradas=entradas)

@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    if not session.get('logado'):
       abort(401)
    titulo = request.form['titulo']
    texto = request.form['texto']
    sql = "INSERT INTO entradas(titulo, texto) VALUES (?, ?)"
    g.bd.execute(sql, [titulo, texto])
    g.bd.commit()# rollback para voltar
    flash("Nova entrada gravada com Sucesso!")
    return redirect(url_for('exibir_entradas'))

# Cria rota login 
@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        print(request.form['username'], request.form['password'])
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logado'] = True
            flash("Login efetuado!")
            return redirect(url_for('exibir_entradas'))
        erro= "Usuário ou senha inválido"
    return render_template("login.html", erro=erro)

# Cria rota logout
@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('exibir_entradas'))
