
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola bienvenido en esta Aplicacion!"