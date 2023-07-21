names = {'Nelson', 'Jenny', 'Alejo', 'Helena', 'Nelson'}
print(names)

# Podemos ver de qué tamaño es el archivo o cuantis elementos tiene el conjunto

size = len(names)
print(size) # En este caso al ejecutarlo me dice que son 4, recordemos que el no tiene en cuenta los duplicados

# Para preguntar por un elemento en especial utilizamos in

print('Nelson' in names) # Rta: True
print('Froilan' in names) # Rta: False

# Para adicionar usamos add

names.add('Froilan')
print(names)

# Para actualizar el conjunto utilizamos update, si intentamos agregar un mismo elemento, el programa no lo tendrá en cuenta

names.update({'Migue', 'Rose', 'Nelson'})
print(names)

# Para eliminar un elemento se utiliza remove o discard, este ultimo se utilizaría para que el programa no genere error si no hay elementos con ese nombre

names.remove('Nelson')
print(names)

names.discard('Nelson')
print(names)

# Para limpiar el conjunto se utiliza clear

names.clear()
print(names)
print(len(names))

# Para realizar operaciones entre conjuntos podemos iniciar con unir conjuntos, se utiliza union o el simbolo |

names_2 = {'Aminta', 'Beatriz', 'Hector'}
names_3 = {'Nelson', 'Alejo', 'Helena', 'Jenni'}

names_union = names_2.union(names_3)
print(names_union)

names_4 = {'Fabian', 'Kim', 'Alex'}
names_5 = {'Mario', 'Paola', 'Adrian'}
print(names_4 | names_5)

# Continuemos con la intersección o intersection, también podemos utilizar el simbolo &

names_2.add('Nelson') # Agregamos el nombre Nelson a names_2
names_5.add('Nelson') # Agregamos el nombre Nelson a names_5
print(names_2)
print(names_5)

names_intersection = names_2.intersection(names_5)
print(names_intersection) # Rta: Nelson
print(names_2 & names_5) # Rta: Nelson

# Ahora veamos diferencia o difference, también se puede utilizar el simbolo -

names_difference = names_2.difference(names_5)
print(names_difference)
print(names_2 - names_5)
