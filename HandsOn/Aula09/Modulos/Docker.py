#!/usr/bin/python
# arquivo: Docker.py

from docker import Client
from ConfigParser import ConfigParser

class Docker:
    def __init__(self):
        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.client = Client(base_url="tcp://%s:2376"%config.get("docker","server"))
        except Exception as e:
            print "Falhou ao conectar com o docker: ",e

    def list_containers(self):
        containers = self.client.containers(all=True)
        return containers

    def create_container(self,name,image):
        container = self.client.create_container(name=name,
                                                 image=image,
                                                 command="/bin/bash",
                                                 stdin_open=True,
                                                 tty=True,
                                                 detach=True)
        self.client.start(container)
        print "Container criado com sucesso!"

    def remove_container(self,name):
        container = self.client.stop(name)
        container = self.client.remove_container(name)
        print "Container removido com sucesso!"

    def exec_command(self,name,cmd):
        exec_id = self.client.exec_create(name,cmd)
        response = self.client.exec_start(exec_id)
        print response
        
    def inspect_container(self,name):
        container = self.client.inspect_container(name)
        print container

if __name__ == '__main__':
    d = Docker()
    d.remove_container("Proxy")
    d.create_container("Proxy","ubuntu")
#    d.exec_command("Proxy","apt-get clean")
#    d.exec_command("Proxy","apt-get update")
#    d.inspect_container("Proxy")







