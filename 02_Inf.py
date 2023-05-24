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