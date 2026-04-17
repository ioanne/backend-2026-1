from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hola amigos!' # HTTP 200 OK

@app.route('/ifts')
def ifts():
    return 'Hola alumnos!' # HTTP 200 OK


# Fragmento de python para que no se ejecute el código app.run
# al import app.py desde otro lado.
if __name__ == '__main__':
    app.run(debug=True, port=8889)

"""
Codigos de error HTTP

"""

"""
HTTP Hypertext transfer protocol

GET -> obtener
Genera un request a un recurso

Get -> / -> response (respuesta)


Podemos hacer una petición a un recurso, alguien (un servidor)
recibe esta petición la procesa y nos devuelve una respuesta.

google.com/images (el recurso es images)
google.com dominio (El dominio se registra)

el dominio es nombre mas facil que una dirección de IP
detras del dominio esta la IP

Hay dos tipos de direcciones de IP:
ipv4 142.251.128.46 -> 2**32 4.294.967.296 posibles direcciones
ipv6 2001:0db8:85a3:0000:0000:8a2e:0370:7334 -> 2**128 posibles direcciones
340.282.366.920.938.463.463.374.607.431.768.211.456


4.294.967.296 / 340.282.366.920,938.463.463.374.607.431.768.211.456 (3,4028236692093846346337460743177e+38)
3,4028236692093846346337460743177e+38


PC -> abro un puerto 8080 y me quedo escuchando



"""