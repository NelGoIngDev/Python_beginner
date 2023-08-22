'''
En este archivo se verá el funcionamiento de las funciones en la programación.
Las funciones se utilizan para ejecutar un conjunto de lineas de codigo definidas.
Vamos a ejecutar un print y luego vreamos nuestro propio print para apreciar la diferencia o la funcionalidad.
'''

print('Hello world')

def my_print():
    print('Hello world this is my print')
    print('This my print. ' * 2) # También se puede multipliar el texto

my_print() # Al ejecutar la función muestra todas las lineas de código que se hayan definido.

# También se le puede asignar un nombre a esa variable igual que la función print, por ejemplo
def my_print(text):
    print(text * 2)

my_print('Este es mi texto')
my_print('No hay que volver a escribir la logica definida en la función, solo hay que ejecutarla y ella hará nuevamente lo definido. ')

# Podemos definir operaciones matemáticas.
def suma(a, b):
    print(a + b)

suma(1, 6) # 7
suma(20, 50) # 70

# Podemos utilizar la función que creamos anteriormente y vemos que pasa.
def suma(a, b):
    my_print(a + b)

suma(1, 6) # 14 lo que hace es ejecutar la multiplicación con los números.
suma(20, 50) # 140