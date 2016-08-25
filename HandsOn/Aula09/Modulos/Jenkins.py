#!/usr/bin/python

import jenkins
from lxml import etree
from ConfigParser import ConfigParser

class Jenkins:
    def __init__(self):
        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.server = jenkins.Jenkins("http://%s:8080"%config.get("jenkins","server"))
            print self.server.get_version()
        except Exception as e:
            print "Nao foi possivel conectar ao jenkins: ",e

    def create_job(self,name,repo_url,cmd):
        try:
            with open("templates/job.xml","r") as f:
                xml = f.read().replace("REPO_URL",str(repo_url))

            xml = self.generate_steps(xml,cmd)

#            print jenkins.EMPTY_CONFIG_XML
            self.server.create_job(name,xml)
            print "Job criado com sucesso!"
        except Exception as e:
            print "Falhou ao criar job: ",e


    def generate_steps(self,xml,cmd):
        root = etree.XML(xml)
        for b in root.findall ("builders"): #procura por elemento builders no root
            builder = b #ponteiro para builders (isolando ele em builder)
        with open (cmd,"r") as f:
            for c in f.readlines():
#        for c in builder.iterchildren():
#            print c.tag, c.text
#            for j in c.iterchildren():
#                print j.tag, j.text

                command = etree.Element("command") #novo elemento
                command.text = 'ssh forlinux@192.168.0.2 "%s"'%c #novo valor #part4 e 5

                shell = etree.Element("hudson.tasks.Shell") #cria elemento (step q cria cmd shell - Jenkins)       
                shell.append(command) #trabalha nos elementos filhos (add cmd)
                builder.append(shell) #trabalha nos elementos filhos (add shell)

        return etree.tostring(root) #converte novamente p. string p. retornar no generate_steps.
        
    def run_job(self,name,var,value): #part6
        try:
            self.server.build_job(name,{var:value})
            print "Job executado!"
        except Exception as e:
            print "Falhou ao executar job: ",e

if __name__ == '__main__':
    j = Jenkins()
#    j.create_job("JobPython")
#    j.create_job("JobEditada")
#    j.create_job("JobDocker")
#    j.create_job("JobDockerSSHAuto") as aspas estavam erradas
#    j.create_job("JobDockerSSHAuto2")
#    j.create_job("JobDockerSSHAuto3") #ja estara parametrizada (alteramos o .xml)
    #    for i in range (1,10): #criara 10 containers
    #        j.create_job("JobCreateContainer%s"%i)
    #        j.run_job("JobCreateContainer%s"%i,"CONTAINER","container%s"%i)
    j.create_job("JobDexter")
#    j.run_job("JobWordpress","CONTAINER","wordpress")
