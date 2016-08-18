#!/usr/bin/python
# arquivo: GruposView.py

# possui a rota (roteamento) somente envia para outro arquivo que executa acoes e traz o resultado.

from flask import Blueprint, jsonify

grupo = Blueprint('grupos',__name__)

@grupo.route("/grupos/",methods=["GET"]) # o methods eh usado para API =listar
def grupos():
    json_response = {"message":"Listagem de todos os grupos"} #dicionario
    return jsonify(json_response)

@grupo.route("/grupos/",methods=["POST"]) # o methods eh usado para API =add
def add_grupos():
    json_response = {"message":"Cadastro de grupos"} #dicionario
    return jsonify(json_response)

@grupo.route("/grupos/<id>/",methods=["PUT"]) # o methods eh usado para API =update
def update_grupos(id):
    json_response = {"message":"Atualiza o grupo"} #dicionario
    return jsonify(json_response)

@grupo.route("/grupos/<id>/",methods=["DELETE"]) # o methods eh usado para API =delete
def delete_grupos(id):
    json_response = {"message":"Deletando o grupo"} #dicionario
    return jsonify(json_response)

@grupo.route("/grupos/<id>/",methods=["GET"]) # o methods eh usado para API =lista grupo especifico
def get_grupos(id):
    json_response = {"message":"Mostrando grupo do ID %s "%id} #dicionario 
    return jsonify(json_response),201 #201 status code
