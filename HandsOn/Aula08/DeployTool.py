#!/usr/bin/python
# arquivo: DeployTool.py
#-----------------------

import yaml
import argparse
from Modulos.Docker import Docker
from Modulos.SSH import SSH

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
        #docker.remove_container(self.arquivo.get("application"))        
        try:
           docker.create_container(self.arquivo.get("application"),"ubuntu")
        except Exception as e:
            print "Container ja existe: ",e
        ssh = SSH()        
        for c in self.arquivo.get("deploy-sequence"):
            print "Executando comando: ",c
            ssh.exec_command(self.arquivo.get("application"),c) #fazer deploy da aplicacao
        #testar aplicacao (ir no navegador

if __name__ == '__main__':
    d = DeployTool()
    args = d.parser.parse_args() #le argumentos passados pelo usuario
#    print "Arquivo de deploy selecionado: ",args.i
    d.yaml_parser(args.i) #converte arquivo yaml em dicionario
    d.deploy() #faz deploy da aplicacao
