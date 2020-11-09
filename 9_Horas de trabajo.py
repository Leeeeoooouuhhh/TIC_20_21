def ejercicio_9():
    horas_totales=input("Cuantas horas trabaja: ")
    precio_normal=30
    precio_extra=45
    if(horas_totales<=40):
        salario=horas_totales*precio_normal
    else:
        salario=40*precio_normal+(horas_totales-40)*precio_extra
    print "Tu salario Kpo: ",salario

ejercicio_9()
    
