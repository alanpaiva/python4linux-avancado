#!/bin/usr/python
# arquivo: run.py
# especialmente para rodarmos a aplicacao..
#

from flask import Flask, jsonify
from Blueprints.UsuariosView import usuario #busca na pasta Blueprints arquivo UsuariosView e pego a blueprint chamada usuario.
from Blueprints.GruposView import grupo

# criar aplicacao flask (basicamente sera sempre o main - app principal do flask) (instanciando)
app = Flask(__name__)
app.register_blueprint(usuario) #registrando bprint usuario
app.register_blueprint(grupo) #registrando bprint grupo

# criar URLs.. "/" eh equivalente a raiz. (index) (criando rotas index)
@app.route("/")
# view
def index(): #nome da view
    return "Pagina index" #retorno qdo cair nessa URL

#executar app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True) #pode ser qualquer porta
# com isso posso fazer um dashboard e mostrar ao cliente..



