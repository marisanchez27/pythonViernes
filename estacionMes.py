#ESTACIONES MESES DEL AÑO 3-2022(EMA322)

estacionMes= input("digite el mes para saber en que estacion estamos: ").lower()

if(estacionMes == "octubre" or estacionMes == "noviembre"):
    print("es OTOÑO")
elif(estacionMes =="diciembre" or estacionMes =="enero" or estacionMes =="febrero" or estacionMes =="marzo"):
    print("es INVIERNO")
elif(estacionMes =="abril" or estacionMes =="mayo"):
    print("es PRIMAVERA") 
elif(estacionMes =="junio" or estacionMes =="julio" or estacionMes =="agosto" or estacionMes =="septiembre"):
    print("es VERANO")
else:
    print("MES INGRESADO NO EXISTE")