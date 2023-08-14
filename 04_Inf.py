'''
Para iniciar con las **list comprehension** debemos tener en cuenta la siguiente sintaxis
[element for element in iterable] a continuación describiré cada parte de esta sintaxis para tener una mejor comprensión
element = es el elemento que vamos a hacer parte de esa lista
for element in iterable = es el ciclo para obtener los elementos de una iteración de una estructura de datos que tengamos definida puede ser una lista, un conjunto o una tupla
'''
# La forma tradicional como se realiza una lista es:
print('List Comprehension')

numbers = []
for element in range(1, 11):
    numbers.append(element * 2) # Podemos decirle al programa que cada elemento sea multiplicado por 2
print('Sintaxis clasica, v1=> ', numbers)

# Ahora aplicando la sintaxis de list comprehension:
numbers_v2 = [element * 2 for element in range(1, 11)]
print('Sintaxis comprehension, v2=> ', numbers_v2)

'''
Ahora podemos empezar a agregar condiciones a esta sintaxis
tengamos en cuenta la siguiente sintaxis para agregar condiciones
Ejemplo:  [i*2 for i in range(1, 101) if i % 2 == 0]
i = elemento
for i in range(1, 101) = es el ciclo para obtener los elementos de una iteración de una estructura de datos
if i % 2 == 0 = es la condición opcional para filtrar elementos
'''
print('List Comprehension con condiciones')

numbers_v3 = []
for i in range(1, 11):
    if i % 2 == 0: # condición si el reciduo de la división entre 2 es igual a cero, entonces lo agrega a la lista
        numbers_v3.append(i * 2) # Podemos decirle al programa que cada elemento sea multiplicado por 2
print('Sintaxis clasica, v3=> ', numbers_v3)

numbers_v4 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print('Sintaxis comprehension, v4=> ', numbers_v4)

print('_' * 52) # Esto se utiliza para que al momento de ejecutar el código en la terminal se vea una "separación" del tema
'''
También se puede aplicar lo anterior a los diccionarios, se llama **Dictionary Comprehension**, la sintaxis es la siguiente
key:value for var in iterable
key:value = elemento llave-valor
for var in iterable = ciclo donde se extraen elementos de cualquier iterable
'''
print('Dictionary Comprehension')
dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print('Sintaxis clasica v1 => ', dict)

dict_v2 = {i : i * 2 for i in range(1, 5)}
print('Sintaxis comprehension v2 => ', dict_v2)

print('_' * 52) # Esto se utiliza para que al momento de ejecutar el código en la terminal se vea una "separación" del tema

# Ahora hagamos una iteración utilizando una lista, primero forma clásica y luego con la sintaxis de Comprehension

import random # Se importa para que genere un numero aleatorio
countries = ['Colombia', 'Mexico,', 'Bolivia', 'Perú']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print('Sintaxis clásica, v1 => ', population)

population_v2 = {country: random.randint(1, 100) for country in countries}
print('Sintaxis comprehension, v2 => ', population_v2)

# Ahora vamos a realizar otro ejemplo con dos listas

names = ['Nelson', 'Jenny', 'Alejo']
ages = [33, 30, 8]

print(list(zip(names, ages))) # zip nos ayuda a unir o realizar la fusión de dos listas, pero debemos indicarle al programa que la necesitamos en una lista

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

print('_' * 52)

# Ahora vamos a poner condiciones
print('Dictionary Comprehension con condiciones')

population_v3 = {country: random.randint(1, 100) for country in countries}
print('Sintaxis comprehension, v3 => ', population_v3)

result = {country: population for (country, population) in population_v3.items() if population > 20}
print(result)