"""
DocString
...
"""
# Comentario

# Variables
numero_entero = 5
numero_flotante = 3.14
cadena = "Hola, mundo!"
verdadero = True # Boolean
falso = False # Boolean
vacio = None # NoneType (ausencia de valor)

lista = [1, 2, 3, 4, 5, "hola", True, None, [6, 7, 8, [[[]]]]]
tupla = (1, 2, 3, 4, 5,  "hola", True, None, [6, 7, 8, [[[]]]])
conjunto = {1, 2, 3, 4, 5, "hola", True, None}
diccionario = {
    "clave1": [1, 2, 3, 4, 5, "hola", True, None, [6, 7, 8, [[[]]]]],
    "clave2": "valor2",
    "clave3": "valor3",
    "print": print,
    "suma": sum
}
diccionario["print"]("Hola")
diccionario["clave1"]
diccionario["clave2"]
diccionario["clave3"]

# condicionales

if cadena == "Hola, mundo!":
    print("La cadena es correcta.") # va a entrar acá
    print()
    print()
    # if dentro de otro if
    if cadena == "Hola, mundo":
        print("La cadena es correcta.")
    else:
        print("La cadena es incorrecta.") # va a entrar acá
print("Estamos fuera del if")


if cadena == "Hola, mundo":
    print("La cadena es correcta.")
else:
    print("La cadena es incorrecta.") # va a entrar acá


if cadena == "Hola, mundo":
    print("La cadena es correcta.")
elif cadena == "Hola, mundo!":
    print("La cadena es correcta en elif.") # va a entrar acá
# infinitos elif.
else:
    print("La cadena es incorrecta.")

# Operadores lógicos
# and, or, not (negación)

# Operador de comparación
# ==, !=, >, <, >=, <=

if 10 > 0:
    print("10 es mayor que 0.")

if 10 < 0:
    print("10 es menor que 0.")
else:
    print("10 no es menor que 0.")

if 10 >= 10:
    print("10 es mayor o igual que 10.")

if 10 <= 10 and 9 <= 9:
    print("10 es menor o igual que 10 y 9 es menor o igual que 9.")

if 10 > 0 or 10 < 0:
    print("10 es mayor que 0 o 10 es menor que 0.")

True and True # True
True and False # False
False and True # False
False and False # False

1 * 1 # 1
1 * 0 # 0
0 * 1 # 0
0 * 0 # 0

True or True # True
True or False # True
False or True # True
False or False # False

1 + 1 # 1
1 + 0 # 1
0 + 1 # 1
0 + 0 # 0

# separar en terminos.

True and False or True and True or False and False
(True and False) or (True and True) or (False and False)

True and (False or True) and True or False and False

# operador de identidad
# is

algo = None
if algo is None:
    print("La variable 'algo' es None.")

if algo is not None:
    print("La variable 'algo' no es None.")

# indentación (la sangría, los 4 espacios)

# Bucleas para iterar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elemento in lista:
    print(elemento)


"""
    Sintaxis del for en java
    for (i=0, i >= 10, i++) {
        ...
        ...
        ...
    }

"""

palabra = "Acá vamos a tener una palabra messi oculta"

palabras = palabra.split(' ')
contador = 0
while contador != len(palabras): # while infinito
    if palabras[contador] == 'messi':
        print("Encontramos la palabra oculta.")
        print(f"El índice de la palabra oculta es: {contador}")
        break # nos sirve para romper el while
    # En los while podemos usar continue (saltea la ejecución)
    contador += 1


numeros = [1,2,3,4,5,6,7,8,9,10]
contador = -1
while contador <= 9:
    contador+=1
    if numeros[contador] % 2 == 0:
        continue # No voy a continuar, dame el próximo
    
    print("Ejecución de otro código")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Ejecucion de codigo")

for i in range(0, 11, 2):
    print("Ejecucion de codigo")


# range es una "función" me devuelve numeros desde 1 inclusive hasta no llegar a 11.

# En python todo es un objeto
print # me muestra algo en consola
dir # me muestra todos los atributos de objetos


def suma(a, b): # a y b son parametros de una función
    return a + b

# Los parametros se pueden pasar por posición o por nombre o por posición y nombre
# Posición
resultado = suma(1, 2)
resultado = suma(1, b=2)
resultado = suma(a=1, b=2)

# Lo que no se puede hacer es pasar por nombre y luego por posición
# resultado = suma(b=1, 2) # Esto no se puede hacer

def foo(a,b,c,d,e,f):
    return a + b + c + d + e + f

resultado = foo(1, 3, 2, f=4, d=5, e=6)

resultado = foo(8, 4, 78, f=123, d=567, e=345)

def division(a, b):
    return a / b

division(10, 2)
# division(10, 0)
division(0, 10)

# division(a=10, b=0)
# division(b=0, a=10)

division(b=10, a=0)

# division(10, a=0) # esta mal, no puedo pasarle 2 valores a a.

# Def es la palabra reservada para crear una función (en otros lenguajes function)
def nombre_funcion(parametro):
    # el bloque que ejecuta mi función
    return parametro

nombre_funcion(1)
nombre_funcion("Hola")
nombre_funcion([1, 2, 3, 4, 5])
nombre_funcion({"clave": "valor"})
nombre_funcion((1, 2, 3, 4, 5))

def funcion(*a):
    print(a)

def funcion2(*a, **b):
    print(a)
    print(b)

funcion2(1,2,3,4,5,6,7,8,9, nombre=1, pepe=2, hola="saludo")

lista = [1,2,3,4,5,6,7]
diccionario = {'nombre': 1, 'pepe': 2, 'hola': 'saludo'}

funcion2(*lista, **diccionario) # el * sirve para desempaquetar la lista y el ** sirve para desempaquetar el diccionario

def funcion3(a,b,c):
    print(a,b,c)

lista = [1,2,3]
diccionario = {'a': 1, 'b': 2, 'c': 3}

funcion3(**diccionario) # el * sirve para desempaquetar la lista

dato = {"id": 5}
def request(**kwargs):
    id = kwargs["id"]

request(**dato)

# por convencion se llama *args para parametros posicionale
# **kwargs para parametros por nombre

@request('/user')
def get_user(*args, **kwargs):
    return 10

#  ejecuta algo acá (identificar de donde viene el request y hacia donde va)
get_user("algo")
# ejecuta algo acá (formatear la salida, es decir la respuesta.)


def mi_decorador(func):
    def envolver():
        print("Hacemos algo antes de mi funcion")
        func()
        print("Hacemos algo despues de mi funcion")
    return envolver

@mi_decorador
def foo():
    print("Esta es mi funcion")
