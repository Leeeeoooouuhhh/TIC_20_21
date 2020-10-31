'''Recibe 2 numeros enteros que son operados segun la variable
S=Suma
R=Resta
M=Multiplicacion
D=Division'''
def operar(numero1,numero2,resultado):
    operaciones={
        "S":"+",
        "R":"-",
        "M":"*",
        "D":"/",
        }
    return eval(str(numero1)+operaciones[resultado]+str(numero2))

print(operar(7,4,"M"))
