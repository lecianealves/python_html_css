# Importa flask e Render template
from flask import Flask, render_template

# Cria app
app = Flask("Hello")

# Cria rota (URL)
@app.route("/hello")
def hello():
    return render_template("hello.html")