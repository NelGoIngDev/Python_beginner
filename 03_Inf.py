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
