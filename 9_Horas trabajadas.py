def calculo_salario(horas):
    input="salario = 0"
    if horas <= 40:
        salario = 30*horas
    else:
        cuarenta_horas = 40*30
        horas_extra = (horas - 40)*45
        salario=cuarenta_horas+horas_extra
        
    return "El salario es: "+str(salario)+"€"

print(calculo_salario(45))
