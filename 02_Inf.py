
print((8/2)+4*8)
print(False and True)
print(int(4.56))
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
print(primos[3])
elements = ['water', 'fire', 'wind', 'earth']
for element in elements:
    print(element)

'''
Los Booleans o boleanos se caracterizan por tener solo 2 respuestas, True o False, en español Verdadero o Falso.
Siempre se debe escribir la palabra True o False con la primera letra en mayúscula, si no se hace genera error.
Para invertir el resultado se escribe al inicio la palabra not.
'''
is_single = True
print(is_single)
print(type(is_single)) # Para ver el tipo de dato que genera => la respuesta es 'bool' que significa boolean

is_single = True
print(is_single)
print(type(is_single))

'''
En la siguiente variable se ejecuta el Boolean False ya que arriba tenemos la misma variable con el valor True y vamos a negar que
sean iguales para gerar el Bollean
'''
is_single = not is_single 
print(is_single)
print(type(is_single))

'''
En la transformación de tipos de datos, podemos convertir un numero en texto, un texto en número o un string en boleano.
print('Ricardo tiene ' + 12 'años') Esto Python no lo va a saber interpretar ya que Python no sabe qué hacer con un 
string y un número entero "int" Entonces veamos los siguientes ejemplos.
'''
name = 'Ricardo'
print(type(name)) # Rta. class 'str' = texto
last_name = 'Quintero Rodriguez'
print(type(last_name)) # Rta. class 'str' = texto
age = 18
print(type(age)) # Rta. class 'int' = 'número'
married = True
print(type(married)) # Rta. class 'bool' = boleano

# Hay dos maneras de convertir los tipos de datos: concatenando con el signo + y utilizando la función de formato f
template = 'v1 = Hola, mi nombre es ' + name + ' y mis apellidos son ' + last_name + ' mi edad es ' + str(age) + ' y mi estado civil es casado ' + str(married)
print(template)

template = f'v2 = Hola, mi nombre es {name} y mis apellidos son {last_name} mi edad es {age} y mi estado civil es casado {married}'
print(template)
