'''
Para iniciar con las **list comprehension** debemos tener en cuenta la siguiente sintaxis
[element for element in iterable] a continuación describiré cada parte de esta sintaxis para tener una mejor comprensión
element = es el elemento que vamos a hacer parte de esa lista
for = es el ciclo para obtener los elementos de una iteración de una estructura de datos que tengamos definida puede ser una lista, un conjunto o una tupla
'''
# La forma tradicional como se realiza una lista es:
numbers = []
for element in range(1, 11):
    numbers.append(element * 2) # Podemos decirle al programa que cada elemento sea multiplicado por 2
print('v1=> ', numbers)

# Ahora aplicando la sintaxis de list comprehension:
numbers_v2 = [element * 2 for element in range(1, 11)]
print('v2=> ', numbers_v2)

'''
Ahora podemos empezar a agregar condiciones a esta sintaxis
tengamos en cuenta la siguiente sintaxis para agregar condiciones
Ejemplo:  [i*2 for i in range(1, 101) if i % 2 == 0]
i = elemento
for = es el ciclo para obtener los elementos de una iteración de una estructura de datos
if = es la condición opcional para filtrar elementos
'''
numbers_v3 = []
for i in range(1, 11):
    if i % 2 == 0: # condición si el reciduo de la división entre 2 es igual a cero, entonces lo agrega a la lista
        numbers_v3.append(i * 2) # Podemos decirle al programa que cada elemento sea multiplicado por 2
print('v3=> ', numbers_v3)

numbers_v4 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print('v4=> ', numbers_v4)
