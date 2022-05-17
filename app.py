# Para rodar serviço flask run
# Importa flask 
from flask import Flask 

# Cria app
app = Flask("Hello")

# Cria rota (URL)
@app.route('/')# Outra rota para o mesmo destino
@app.route("/hello") # Recurso do flask que usa URL chamando função
def hello(): # Função a ser chamada
    return "Hello World"

# Nova rota 
@app.route('/tchau')
def tchau():
    return "Tchau"

