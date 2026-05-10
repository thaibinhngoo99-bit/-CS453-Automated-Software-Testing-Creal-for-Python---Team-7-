#contextos

from flask import Flask
import flask
app = Flask(__name__)

## 1 Configuração

### Add configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://"

### Registrar Rotas

@app.route("/path")
def funcao():
    pass
# ou
app.add_url_rule("/path", funcao)

### Inicializar extensões

#from flask_admin import Admin
#Admin.init_app(app)

### Registrar Blueprints
app.register_blueprint(...)

### add hooks

@app.before_request(...)
@app.errorhandler(...)

### Chamar outras factories

#views.init_app(app)


## 2 App Context

### App está pronto! 'app'

### Testar
#app.test_client
# debug
# objetos globais do flask
# (request, session, g)
#- Hooks



## 3 Request Context

### usar globais do flask