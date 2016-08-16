#!/usr/bin/python
#
# arquivo: consumindo_api.py
# data: 15/Aug/2016
# feito por: Alan

'''
 Task 01 - Criando um novo usuario
Foi contratado um novo colaborador na Empresa Dexter e necessario cadastra-lo no sistema de usuarios.
Voce precisara fazer isso atraves da API do sistema.

Esses sao os dados do novo usuario:
Nome: Rafael Medeiros
Email: rafael.medeiros@dexter.com.br

Mas antes de cadastrar, voce precisa verificar se ja existe um usuario ja cadastrado com esse email.
Caso exista, voce precisa remove-lo e depois cadastrar.
'''
import requests
import json

CABECALHO={"Content-Type":"application/json"}
novo = {"nome":"Rafael Medeiros","email":"rafael.medeiros@dexter.com.br"}

todos = requests.get("http://127.0.0.1:5000/usuarios/")._content
todos = json.loads(todos)

#list compreension

lista = [usuario for usuario in todos.get("usuarios") if usuario.get("email") == novo.get("email")]

if lista:
    print "Usuario ja cadastrado!"
    response = requests.delete("http://127.0.0.1:5000/usuarios/%s/"%lista[0].get("id"))
    print response._content
    
response = requests.post("http://127.0.0.1:5000/usuarios/",data=json.dumps
                        (novo),headers=CABECALHO)._content
print response

'''
# Trazendo so os usuarios:
#for usuario in todos.get("usuarios"):
#    print usuario

for usuario in todos.get("usuarios"):
    if usuario.get("email") == novo.get("email"):
        print "Usuario ja cadastrado!"
        response = requests.delete("http://127.0.0.1:5000/usuarios/%s"%usuario.get("id"))
        print response._content
response = requests.post("http://127.0.0.1:5000/usuarios/",data=json.dumps
                        (novo),headers=CABECALHO)._content
print response
'''
