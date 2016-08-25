#!/usr/bin/python
# arquivo: DeployTool.py
#-----------------------

import yaml
import argparse
from Modulos.Docker import Docker
from Modulos.Gitlab import Gitlab
from Modulos.Jenkins import Jenkins

class DeployTool:
    def __init__(self):
        self.parser = argparse.ArgumentParser() #instancia do argumentParser
        self.parser.add_argument("-i",help="Define arquivo de deploy")
        
    def yaml_parser(self,arquivo):
        with open(arquivo,"r") as f:
            self.arquivo = yaml.load(f.read())

    def deploy(self):
#        print self.arquivo
        docker = Docker() #criar container no docker
        jenkins = Jenkins()
        gitlab = Gitlab()
        application = self.arquivo.get("application")
        devs = self.arquivo.get("developers")
        #docker.remove_container(self.arquivo.get("application"))        
        try:
            if gitlab.create_projects(application):
                print "Projeto criado com sucesso!"
            else:
                print "Falhou ao criar projeto"
            for d in devs:
                if gitlab.create_user(d.split("@")[0],d):
                    print "Usuario criado com sucesso!"
                if gitlab.add_user_project(d,application):
                    print "Usuario adicionado ao projeto!"
            webhook = gitlab.add_webhook(application,"http://192.168.0.4:8080/gitlab/build_now")
            if webhook:
                print "Webhook adicionada com sucesso!"
            repo_url = gitlab.get_repo_url(application)
            jobname = self.arquivo.get("job").get("name")
            cmd = self.arquivo.get("job").get("deploy")
            #repo_url = "repo"
            jenkins.create_job(jobname,repo_url,cmd)
            docker.create_container(application,"ubuntu")
        except Exception as e:
            print "Container ja existe: ",e
    
if __name__ == '__main__':
    d = DeployTool()
    args = d.parser.parse_args() #le argumentos passados pelo usuario
#    print "Arquivo de deploy selecionado: ",args.i
    d.yaml_parser(args.i) #converte arquivo yaml em dicionario
    d.deploy() #faz deploy da aplicacao
