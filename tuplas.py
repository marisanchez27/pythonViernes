#creando tuplas en python, se utilizan parentesis ()

estudiantes=("carlos", "rodrigo")
print(estudiantes)


# estudiantes.append("Mari")
# print(estudiantes) esto es un error

#recorriendo tuplas

for estudiante in estudiantes:
    print(estudiante)


#convertir tupla en lista

listaEstudiante=list(estudiantes)
print(listaEstudiante)
listaEstudiante.append("lUZ")
newTuple=tuple(listaEstudiante)
print(newTuple)