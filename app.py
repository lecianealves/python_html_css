# Importa flask
from flask import Flask

# Cria app
app = Flask("Hello")

# Cria rota (URL)
@app.route("/hello")
def hello():
    return "Hello World"