
#En estaprimera parte vamos a ver de forma breve como funciona print, type y los números enteros.

# con 3 comillas se puede digitar una nota de varias lineas y el # sirve para poner una nota en una sola linea.
# Esto permite dejar notas informativas y que al momento de ejecutar el programa no refleje errores, que el programa ignore esto.

'''
Para ver la respuesta en la terminal o cómo quedó la linea de código se utiliza el comando print.
Las variables se definen fácilmente, asignando un nombre y el valor (Ej: name = 'Rodrigo').
Para definir los string se utiliza comilla sencilla ('letras') o comilla doble ("letras").
El comando type se utiliza para ver qué tipo de dato es el que está arrojando el programa.
'''

text = 'Hola mundo'
print(text)
print(type(text)) # Rta: class 'str' (str es la abreviatura de string)

'''
Con los string también se puede concatenar de varias maneras.
En Python existen reglas de escritura con el fin de dar un orden a todo, por ejemplo, las variables se separan con un guion bajo, se puede 
escribir con guion al medio, pero como lo dije anteriormente, son reglas de escritura. (Ej: last_name)
'''

name = 'Nelson'
last_name = 'Gómez'

full_name = name + ' ' + last_name
print('Esta es una concatenación utilizando "+" =>', full_name)

# Otra manera de realizar concatenaciones con frases: template o en español plantilla

template = 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name
print(template)

# Otra opción de formato es: utilizando {}

template2 = 'Hola, mi nombre es {} y mi apellido es {}'.format(name, last_name)
print('v2 =>', template2)

# Y por ultimo hay otra manera más abreviada de digitarlo: al inicio se digita la "f" de format

template3 = f'Hola, mi nombre es {name} y mi apellido es {last_name}'
print('v3 =>', template3)

#Con print tambíen se puede ver el resultado de operaciones matemáticas
suma = 2+5 # Los números o enteros no llevan comillas, de esta manera se le dice al programa el tipo de dato.
print(suma) # suma
print(type(suma)) # int es la abreviatura de integer que significa entero en español.
# Dentro de cada operación se le puede agregar un texto, esto sirve para identificar lo que se ejecuta.
# Recuerde separarlos con una coma.
print('Resta =>', 2-5)
print('Multiplicación =>', 2*5)
print('División =>', 2/5)
print('División con valor entero =>', 29//5)
print('Exponenciación =>', 2**5)
print('Modulo o residuo =>', 3%15)

print('Esta es una operación combinada =>', ((5//2)+3*4)+25+4-46+500)

'''
Cunado se realizan varias operaciones matemáticas en una sola linea hay que tener en cuenta 
la regla o el orden en que estás se desarrollan, para eso se puede recordar en una palabra:
P E M D A S
1. Parentesis
2. Exponentes
3. Multiplicación
4. División
5. Adición
6. Sustracción o Resta
'''
