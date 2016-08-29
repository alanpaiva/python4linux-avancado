#!/usr/bin/python

import boto3

ec2 = boto3.resource("ec2")

def list_instances():
    instances = ec2.instances.all()
    #instances = ec2.instances.filter(Filters[{"Name":"instance-state-name",
    #                                            "Values":["terminated"]}]) #running #stopped

    for i in instances:
        print i
    #    print i.id, i.instance_type 

def create_instance():
    global ec2
    new_isntance = ec2.create_instances(ImageId="ami-2d39803a",
                                        MinCount=1,
                                        MaxCount=1) #range de isntancias que queremos criar
    return new_instance

def search_instance(id)
#    instances = ec2.instances.filter(Filters[{"Name":"InstanceIds",
                                             "Values":[id]}]) #running #stopped
    instances = ec2.instances.filter(Instances=[id]) #running #stopped
    return instances
print "Encontrado", serach_instance("i-03ec6a8f67e0bbec7") #.terminated() #execluiria a instancia..

print create_instance()
#print list_instances()

def create_sg(name): #criando security groups
    sg = ec2.create_security_group(GroupName="Python-SG",
                                    Description="Grupo criado na aula"
    return sg

def add_rule (sg.rule):
    sg = ec2.SecurityGroup(sg)
    sg.authorize_ingress(FromPort=80, ToPort=80, CidrIp="0.0.0.0/0", IpProtocol="tcp")
    return sg

def del_rule (sg.rule):

#print add_rule("sg-cda21cb7")
print add_rule("sg-cda21cb7")
print create_sg("Python-SG")
    


