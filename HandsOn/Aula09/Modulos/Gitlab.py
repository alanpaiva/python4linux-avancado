#!/usr/bin/pyhon

import requests
import json
from ConfigParser import ConfigParser

class Gitlab:
    def __init__(self):
        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.token = config.get("gitlab","token")
            self.server = config.get("gitlab","server")
        except Exception as e:
            print "Falhou ao pegar configuracoes: ",e    
    # metodos privados para a classe
    # efetua a requisicao e traz algum valor (params sao opcionais no get)
    def _make_get(self,resource,params=""):
        url = "http://{2}/api/v3/{0}?private_token={1}"\
               .format(resource,self.token,self.server) #metodo format para trabalhar com strings
        response = requests.get(url)
        return response
    
    #     (data eh obrigatorio no post)
    def _make_post(self,resource,data):
        url = "http://{2}/api/v3/{0}?private_token={1}"\
               .format(resource,self.token,self.server)
        headers  = {"Content-Type":"application/json"}
        response = requests.post(url,data=json.dumps(data),headers=headers) 
        #data do requests, data que recebeu /// json.dumps -> converte dicionario para string
        return response


    def get_users(self):
        users = self._make_get("users")
        users = json.loads(users._content) # converte a string em dicionario
        return users
        # para trazer na tela nome e email somente (sem formato json)
#        for u in users:
#            print u.get("name"), u.get("email")

    def get_projects(self):
        projects = self._make_get("projects")
        projects = json.loads(projects._content) # converte a string em dicionario
        return projects

    def create_user(self,name,email):
        user_data = {"name":name,
                     "username":name,
                     "email":email,
                     "password":"!23Mudar"}
        user = self._make_post("users",user_data) #dois param: URL e dados que enviaremos via POST
        if user.status_code == 201: #201=created
            return True
        else:
            print user._content
            #print user.status_code
            return False

    def create_projects(self,name):
        projects_data = {"name":name}
        projects = self._make_post("projects",projects_data) #dois param: URL e dados que enviaremos via POST
        if projects.status_code == 201: #201=created
            return True
        else:
            print projects._content
            #print projects.status_code
            return False

    def add_user_project(self,user_email,project_name):
        projects = self.get_projects()
        users = self.get_users()
        p = [p for p in projects if p.get("name") == project_name ]
        u = [u for u in users if u.get("email") == user_email ]
        print "id projeto",p
        print "id usuario",u
        if not p:
            print "Projeto nao encontrado!"
            return False
        if not u:
            print "Usuario nao encontrado!"    
            return False
        data = {"id":p[0].get("id"),
                "user_id":u[0].get("id"),
                "access_level":30}
        response = self._make_post("projects/%s/members"%p[0].get("id"),data)
#        print response.status_code,response._content
        if response.status_code == 201:
            return True
        else:
            return False

    def add_webhook(self,project_name,url):
        data = {"url":url, "push_events":True} # dados que enviaremos para a request
        projects = self.get_projects()        
        p = [p for p in projects if p.get("name") == project_name ]
        if not p:
            print "Projeto nao encontrado!"
            return False
        response = self._make_post("projects/%s/hooks"%p[0].get("id"),data)
        if response.status_code == 201:
            return True
        else:
            return False

    def get_repo_url(self,project_name):
            projects = self.get_projects()
            print project_name
            p = [p for p in projects if p.get("name") == project_name ]
            print p
            if not p:
                print "Projeto nao encontrado!"
                return False
            repo_url = p[0].get("ssh_url_to_repo")
            return repo_url #para retornar no Jenkins como string..



if __name__ == '__main__':
    g = Gitlab()
    #g.get_users()
    #print g.get_projects()

# Teste criacao usuarios:
    if g.create_user("Malandramente","malandramente@cv.com.br"):
        print "Usuario criado com sucesso!"
    else:
        print "Falhou ao criar usuario!"

# Teste criacao projetos:
#    if g.create_projects("ProjetoLlhouco2"):
#        print "Projeto criado com sucesso!"
#    else:
#        print "Falhou ao criar projeto!"

# Teste de encontrar usuario para projeto:
#    g.add_user_project("jota@tes.com.br","ProjetoLlhouco")

# Teste do hook
#    if g.add_webhook("ProjetoLlhouco","http://urlteste.com.br:8080"):
#        print "Webhook adicionada com sucesso"
#    else:
#        print "Falhou ao adicionar webhook"
