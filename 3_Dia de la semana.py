def dia_de_la_semana(num):
    if num >= 1 and num <= 7:
        dias=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
        return dias[(num)-1]
    else:
        return"no_apto"
dia_semana=dia_de_la_semana(input("Introduce un numero entre 1 y 7: "))
if dia_semana=="no_apto":
    print"Esto no me sirve,pon otro valor"
else:
    print"El dia que has introducio es "+dia_semana


