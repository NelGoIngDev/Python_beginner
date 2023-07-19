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
sean iguales para gerar el Boolean
'''
is_single = not is_single 
print(is_single)
print(type(is_single))

'''
En la transformación de tipos de datos, podemos convertir un numero en texto, un texto en número o un string en booleano.
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
'''
Hay dos maneras de **convertir los tipos de datos**: escribiendo la abreviación de string "str" o integer "int"
a continuación veremos cómo convertimos la edad que es un entero en cadena de texto para unir los datos en la oración.
'''
template = 'v1 = Hola, mi nombre es ' + name + ' y mis apellidos son ' + last_name + ' mi edad es ' + str(age) + ' y mi estado civil es casado ' + str(married)
print(template)

template = f'v2 = Hola, mi nombre es {name} y mis apellidos son {last_name} mi edad es {age} y mi estado civil es casado {married}'
print(template)


# Los **operadores de comparación** se utilizan para indicar al programa las diferencias de los valores, las respuestas van a ser True o False

print(1 > 2) # 1 es mayor que 2 = Rta: False
print(7 > 3) # 7 es mayor que 3 = Rta: True
print(3 < 5) # 3 es menor que 5 = Rta: True
print(4 < 2) # 4 es menor que 2 = Rta: False
print(7 == 7) # 7 es igual que 7 = Rta: True ; Para decir que algo es igual que, se digita doble simbolo igual
print(7 == 8) # 7 es igual que 8 = Rta: False
print(10 >= 1) # 10 es mayor o igual que 1 = Rta: True
print(10 >= 10) # 10 es mayor o igual que 10 = Rta: True
print(3 <= 1) # 3 es menor o igual que 1 = Rta: False
print(2 != 3) # 2 es diferente que 3 = Rta: True
print(3 != 3) # 3 es diferente que 3 = Rta: False


# En los **Operadores Logicos** encontramos el and, or y not.

print('True and True =>', True and True ) # Rta: True, la única manera que el resultado sea True es que ambas partes se cumplan
print('True and False =>', True and False) # Rta: False
print('False and True =>', False and True) # Rta: False
print('False and False =>', False and False) # Rta: False

print('True or True =>', True or True) # Rta: True
print('True or False =>', True or False) # Rta: True, con or pasa algo diferente, si una de las dos cumple es True
print('False or True =>', False or True) # Rta: True
print('False or False =>', False or False) # False

print('Negando el True =>', not True) # Rta: False
print('Negando el False =>', not False) # Rta: True
