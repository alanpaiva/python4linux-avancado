#!/usr/bin/python
#
# arquivo: consumindo_api.py
# data: 15/Aug/2016
# feito por: Alan

import requests
# Fazendo uma request como se estivesse no navegador:
#response = requests.get("http://127.0.0.1:5000/usuarios/")

#print response
# executando, retorno:
#forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
#<Response [200]>

#print response.__dict__
# executando, retorno:
'''
forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
{'cookies': <RequestsCookieJar[]>, '_content': '{\n  "usuarios": [\n    {\n      "email": "jax@4linux.com.br", \n      "id": 3, \n      "nome": "Jax Teller"\n    }, \n    {\n      "email": "alisson@4linux.com.br", \n      "id": 4, \n      "nome": "Alisson Machado"\n    }, \n    {\n      "email": "corey.taylor@dexter.com.br", \n      "id": 5, \n      "nome": "Corey Taylor"\n    }, \n    {\n      "email": "mega.man@dexter.com.br", \n      "id": 6, \n      "nome": "Mega Man"\n    }\n  ]\n}', 'headers': {'date': 'Mon, 15 Aug 2016 23:19:22 GMT', 'content-length': '420', 'content-type': 'application/json', 'server': 'Werkzeug/0.11.3 Python/2.7.9'}, 'url': u'http://127.0.0.1:5000/usuarios/', 'status_code': 200, '_content_consumed': True, 'encoding': None, 'request': <PreparedRequest [GET]>, 'connection': <requests.adapters.HTTPAdapter object at 0x7fce59d87e90>, 'elapsed': datetime.timedelta(0, 0, 10053), 'raw': <requests.packages.urllib3.response.HTTPResponse object at 0x7fce59d2a450>, 'reason': 'OK', 'history': []}
'''

#print response._content
#executando, retorno:
'''
{
  "usuarios": [
    {
      "email": "jax@4linux.com.br", 
      "id": 3, 
      "nome": "Jax Teller"
    }, 
    {
      "email": "alisson@4linux.com.br", 
      "id": 4, 
      "nome": "Alisson Machado"
    }, 
    {
      "email": "corey.taylor@dexter.com.br", 
      "id": 5, 
      "nome": "Corey Taylor"
    }, 
    {
      "email": "mega.man@dexter.com.br", 
      "id": 6, 
      "nome": "Mega Man"
    }
  ]
}
'''

#print response._content, response.status_code
#executando, retorno:
'''
{
  "usuarios": [
    {
      "email": "jax@4linux.com.br", 
      "id": 3, 
      "nome": "Jax Teller"
    }, 
    {
      "email": "alisson@4linux.com.br", 
      "id": 4, 
      "nome": "Alisson Machado"
    }, 
    {
      "email": "corey.taylor@dexter.com.br", 
      "id": 5, 
      "nome": "Corey Taylor"
    }, 
    {
      "email": "mega.man@dexter.com.br", 
      "id": 6, 
      "nome": "Mega Man"
    }
  ]
} 200
'''

# Buscando usuario especifico:

#response = requests.get("http://127.0.0.1:5000/usuarios/6/")
#print response._content, response.status_code


# Cadastrando novo usuario
import json
#novo = {"nome":"Goku","email":"sayajin@dexter.com.br"}
#response = requests.post("http://127.0.0.1:5000/usuarios/",
#                         data=json.dumps(novo))
#print response._content
'''
forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
{
  "message": "Ocorreu um erro: 'NoneType' object has no attribute '__getitem__'", 
  "status": 1
}

'''
# Desta forma temos o conteudo do cabecalho, portanto nao teremos o erro acima.
#novo = {"nome":"Goku","email":"sayajin@dexter.com.br"}
#cabecalho = {"Content-Type":"application/json"}
#response = requests.post("http://127.0.0.1:5000/usuarios/",
#                         data=json.dumps(novo),headers=cabecalho)
#print response._content
'''
forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
{
  "message": "Usuario cadastrado com sucesso"
}

'''

# Fazendo um PUT
#cabecalho = {"Content-Type":"application/json"}
#novo = {"nome":"Rockman","email":"rockman@dexter.com.br"}
#response = requests.put("http://127.0.0.1:5000/usuarios/6/",
#                        data=json.dumps(novo), headers=cabecalho)
#print response._content
'''
forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
{
  "email": "rockman@dexter.com.br", 
  "id": 6, 
  "nome": "Rockman"
}

'''

# Fazendo um delete
#response = requests.delete("http://127.0.0.1:5000/usuarios/3/")
#print response._content
'''
forlinux@developer  ~/4521-Python/HandsOn/Aula01 (master) $ python consumindo_api.py 
{
  "message": "Usuario deletado com sucesso!"
}
'''

# tapioca wrapper no github..
# https://github.com/vintasoftware/tapioca-wrapper
# https://github.com/vintasoftware/tapioca-facebook


