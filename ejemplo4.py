numeros=[]

tamano=int(input("Ingrese el tamaño: "))

for i in range(tamano):
    numero=int(input("Ingrese un numero: "))
    numeros.append(numero)

buscar=int(input("Ingrese el numero que busca: ")) 
if(buscar in numeros):
    print(f"el numero: {buscar} si esta")
else:
     print(f"el numero: {buscar} No esta")  