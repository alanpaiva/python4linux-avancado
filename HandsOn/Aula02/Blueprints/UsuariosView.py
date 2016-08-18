#!/usr/bin/python
# arquivo: UsuariosView.py

# possui a rota (roteamento) somente envia para outro arquivo que executa acoes e traz o resultado.

from flask import Blueprint, jsonify, request
from Models.Model import Usuarios as UsuariosModel
import json

usuario = Blueprint('usuario',__name__)

@usuario.route("/usuarios/",methods=["GET"]) # o methods eh usado para API =listar
def usuarios():
    todos = UsuariosModel.objects().to_json() # listando todos os users do banco MongoDb
    #print todos #debug
    todos = json.loads(todos)
    json_response = {"usuarios":"todos"} #dicionario
    return jsonify(todos)

@usuario.route("/usuarios/",methods=["POST"]) # o methods eh usado para API =add
def add_usuarios():
    data = request.get_json()
    novo = UsuariosModel()
#    novo.nome = data.get("nome")
#    novo.email = data.get("email")
    for k in data.keys(): # traz as chaves do dicionarios (subst. os 2 itens comentados acima p. apresentacao web)
        setattr(novo,k,data.get(k))    
    novo.save()
    json_response = {"message":"Usuario cadastrado com sucesso!"} #dicionario
    return jsonify(json_response)

@usuario.route("/usuarios/<id>/",methods=["PUT"]) # o methods eh usado para API =update
def update_usuarios(id):
    data = request.get_json()
    u = UsuariosModel.objects(id=id).first()
    for k in data.keys():
        setattr(u,k,data.get(k))
    u.save()
    response = {"message":"Usuario atualizado com sucesso"} #dicionario
    return jsonify(response)

@usuario.route("/usuarios/<id>/",methods=["DELETE"]) # o methods eh usado para API =delete
def delete_usuarios(id):
    u = UsuariosModel.objects(id=id).first()    
    if not u:
        return jsonify({"message":"Usuario nao encontrado"}), 404
    u.delete()
    response = {"message":"Usuario removido com sucesso"} #dicionario
    return jsonify(response)

@usuario.route("/usuarios/<id>/",methods=["GET"]) # o methods eh usado para API =lista user especifico
def get_usuarios(id):
    u = UsuariosModel.objects(id=id).first()
    if not u:
        return "Usuario nao encontrado", 404
    u = json.loads(u.to_json())
    return jsonify(u)
    
    #json_response = {"message":"Mostrando usuario do ID %s "%id} #dicionario 
    #return jsonify(json_response),201 #201 status code
