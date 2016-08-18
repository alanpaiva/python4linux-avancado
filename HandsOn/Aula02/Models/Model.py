#!/bin/usr/python

from flask import Flask
from flask_mongoengine import MongoEngine #importando mongo engine
from datetime import datetime #eh do python nada a ver com o flask **

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"} # conf que conecta no db da app

db = MongoEngine(app) #criamos instancia do banco

class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True) #so pode ter um unico email por nome de user
    date_cadastro = db.DateTimeField(default=datetime.now()) #nao eh do mongoEngine precisa de import **

class Grupos(db.Document):
    nome = db.StringField(unique=True) #so pode ter um unico nome de grupo
    integrantes = db.ListField()
    
#if __name__ == "__main__":
#    u = Usuarios()
#    u.nome = "Alan"
#    u.email = "alan@4linux.com.br"
#    u.save()

if __name__ == "__main__":
    g = Grupos()
    g.nome = "Analistas"
    g.integrantes.append("Alan")
    #g.save()
    # fazer uma busca na classe Grupos e mostrar o grupo cadastrado acima apos exec. Model.py no cmdline:
    todos = Grupos.objects()
    for g in todos:
        print g.nome

    buscado = Grupos.objects(nome="Analistas").first()
    print buscado.nome # nome dos grupos
    print buscado.integrantes # nome dos integrantes
    #print buscado.nome = "Comercial" #= "Comercial"(forma de busca)
    
