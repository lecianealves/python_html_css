# Importa flask
from flask import Flask

#Cria app
app = Flask("Hello")
#

@app.route("/hello")
def hello():
    return "Hello World"