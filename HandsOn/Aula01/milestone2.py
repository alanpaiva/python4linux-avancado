#!/usr/bin/python
#
# arquivo: consumindo_api.py
# data: 15/Aug/2016
# feito por: Alan

import requests
import json

novos_usuarios = [
    "Joao Mendes",
    "Joaquim Seferino",
    "Nicolas Farias",
    "Rodrigo Marcelo",
    "Maria Joana",
    "Abdias Moraes",
    "Eliana Sorriso",
    "Hellen Gonzaga",
    "Humberto Sales",
    "Benedito da Silva"
    ]

for usuario in novos_usuarios:
    nome = usuario
    email = nome.replace(" ",".").lower()+"@dexter.com.br"
    data = {"nome":nome,"email":email}
    headers = {"Content-Type":"application/json"}  
    response = requests.post("http://127.0.0.1:5000/usuarios/",
                                data=json.dumps(data),
                                headers=headers)
    print response._content
