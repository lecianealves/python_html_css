# Flask : Werkzeug + Jinja
# Comandos:
# -> pip install flask - Instala Flask
# -> flask --version
# Cria código 
# -> flask run (Para rodar serviço flask run)
# -> pip freeze > requirements.txt (Cria arquivo de dependencias sm NPM javascript)
# -> pip install python-dotenv
# -> pip freeze > requirements.txt (Atualiza dependencias)
# -> $Home $USER $Path
# Comandos Git: 
# -> git add .
# -> git commit -m "Comentário aqui"
# -> git push

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

