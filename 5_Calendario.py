def calendario():
    dia=input("Introduce el dia entre 1 y 31: ")
    if dia<1 or dia>31:
        print("El numero que has dado no es apto")
        dia=input("Introduzca un dia apto: ")

    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    numero=input("Introduce un mes entre 1 y 12: ")
    if numero<1 or numero>12:
        print("El mes introducido no existe")
        numero=input("Introduzca un mes apto: ")
    mes=meses[numero-1]
    
    ano=input("Introduce un año: ")

    print("La fecha que ha dado es: "),dia,"/",mes,"/",ano

calendario()
