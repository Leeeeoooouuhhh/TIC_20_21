'''Dime un n�mero entre 1 y 10 y lo adivino'''
def adivino():
    numero=input("Dime un numero del 1 al 10: ")

    intento=input("Intentalo mi pana: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado peque�o"
        intento=input("Intentalo mi pana: ")
    print "Ahora has acertado prro"

adivino()
    
