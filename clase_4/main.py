import json

dato = {
    "nombre": "Pedro",
    "apellido": "Perez",
    "edad": 25,
    "mayor_edad": True,
}
dato_json = json.dumps(dato)
print(dato_json)

class Persona:
    nombre = None
    apellido = None
    edad = None
    mayor_edad = None


class Persona:
    def __init__(self, nombre, apellido, edad, mayor_edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mayor_edad = mayor_edad

persona = Persona(**dato)
pp = persona.__dict__
print(pp)