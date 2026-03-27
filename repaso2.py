def mi_decorador(func):
    def envolver():
        print("Hacemos algo antes de mi funcion")
        func()
        print("Hacemos algo despues de mi funcion")
    return envolver

@mi_decorador
def foo():
    print("Esta es mi funcion")

foo()


def validador_de_division(func):
    def envolver(a, b):
        if (b != 0):
            func(a, b)
        print("No se puede dividir por 0, devuelvo 0")
        return 0
    return envolver

@validador_de_division
def dividir(a, b):
    return a / b

class Auto:
    # Hay que tener cuidado
    instancias_creadas = {
        'cantidad': 0
    }
    def __init__(self, marca, modelo, color):
        # Las variables de instancias se crean dentro de self.
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.instancias_creadas["cantidad"] = self.instancias_creadas["cantidad"] + 1

auto1 = Auto(marca="Ford", modelo="Fiesta", color="rojo")



class Moto:
    instancias = [] # Warning (estar atentos)
    def __init__(self):
        self.instancias.append(self)




class Foo:
    atributo_de_clase = 1

    def __init__(self, a, b, c):
        # Atributos de instancia
        self._a = a # atributo de instancia privado (comienza con _)
        self.b = b
        self.c = c

    @property
    def a(self): # getter
        return self._a

    def set_a(self, nuevo_valor): # setter
        self._a = nuevo_valor

class Foo2(Foo):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.pepe = 10

    def editar_a(self, nuevo_valor):
        self._a = nuevo_valor # ESTO NO ESTA BIEN.
        self.set_a(nuevo_valor) # Esto es lo que esta bien, edito a con set_a