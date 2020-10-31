def mes_del_ano():
    num=int(input("Introduce un numero entre 1 y 12: "))
    if num>=1 and num<=12:
        mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        print("El mes que has introducido es :"+mes[num-1])
    else:
        print("No es apto, dame un valor que sirva: ")
        mes_del_ano()   

mes_del_ano()
    
