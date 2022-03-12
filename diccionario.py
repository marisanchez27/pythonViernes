#un diccionario NO se escribe en plural, y es una variable para el diccionario se utiliza las {llaves}, los atributos van en comillas string

estudiante={
    'nombre':'Falcao',
    'edad': 24,
    'esFutbolista': True
}

#imprimir / acceder a todas las llaves
#atributos de mi diccionario
print(estudiante)
#necesito acceder a un atributo o llave del diccionario
print(estudiante['edad'])
print(estudiante.get('nombre'))

#recorrer un diccionario
# y obtener sus valores

for valor in estudiante.values():
    print(valor)