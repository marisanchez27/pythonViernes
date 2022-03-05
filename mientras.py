#importar librerias(recetas/codigos prefabricados)
import math

#variable controladora


#declaro el bucle/ciclo/iteracion/repeticion/la vuelta/loop
#menu
print("Empanadas el machetito")
print("******")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un #")
print("2. Digita 2 para calcular la potencia 2 de un #")
print("******")
opcion=int(input("digita una opcion: "))

while(opcion !=0):
    #variable controladora
    opcion=int(input("digita una opcion: "))
    #pregunte por la opcion
    if(opcion ==0):
        break
    elif(opcion ==1):
        numero=int(input("digita un numero: "))
        raiz=math.sqrt(numero)
        print(f"la raiz de {numero} es {raiz}")
    elif(opcion ==2):
        numero=int(input("digita un numero: "))
        potencia=math.pow(numero,2) 
        print(f"la potencia es {potencia}") 
    else:
        print("No VALIDO")      
        

# while(numero<=20):
#     # print("No importa ")
#     # print(numero)
#     numero+=1

