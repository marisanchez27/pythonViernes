from pickle import TRUE


numeros = []

for i in range(0,5,1):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

numeroBuscado = int(input("Ingrese el numero a buscar: "))

loTengo = False
for i in range(0,5,1):
    if(numeroBuscado == i):
        loTengo = True
        break
    else:
        loTengo = False

if(loTengo != False):
    print("si esta")
else:
    print("no esta")    