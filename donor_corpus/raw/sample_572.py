# Antes de mais nada install o flask = pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Essa é minha HomePage'

@app.route('/contatos')
def contatos():
    return 'Essa são os meus contatos'

app.run()