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
# Una operación matematica tradicional sería así:
a = 1
b = 2
suma = a + b
print(suma)

# La operación suma con utilizando función sería de la siguiente manera
def suma(a, b):
    print(a + b)

suma(1, 6) # 7
suma(20, 50) # 70

# Podemos utilizar la función que creamos anteriormente y vemos que pasa.
def suma(a, b):
    my_print(a + b)

suma(1, 6) # 14 lo que hace es ejecutar la multiplicación con los números.
suma(20, 50) # 140

snake = '''
       /^\/^\\
     _|__|  O|
\/ \/   /~     \/
 \____|_________/
        \_______)
        __//___//
       (_______(
'''
print(snake) # Esto es para separar el tema al ejecutar los resultados en la terminal

# Función return, para explicar esta sección veremos la forma tradicional y después aplicando funciones
suma = 0
for x in range(1, 10): # Le decimos al programa que sume consecutivamente desde el 1 hasta el 10 (1+2+3+4+5+6+7+8+9+10 = 45)
    suma += x
print(suma)

# Ahora aplicando funciones sería de la siguiente manera
def sum_with_range(min, max): # Podemos asignar parámetros min y max
    print(min, max) # Se imprime los rangos sin el resultado
    sum = 0
    for x in range(min, max):
        sum += x
    return sum # Retorna la suma con el calculo total

result = sum_with_range(10, 60) # de esta manera podemos ejecutar la misma logica solo con llamar la función y asignarle parámetros
print(result) # Con esto estamos imprimiendo el resultado 
result_2 = sum_with_range(result, result + 1000) # acá utilizamos el resultado anterior como rango y le indicamos que al resultado anterior le sume 1.000
print(result_2)


