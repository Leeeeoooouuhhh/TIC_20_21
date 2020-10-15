'''Dime un número entre 1 y 10 y lo adivino'''
import random

def adivino_2():
    maxn=1000
    numero=random.randint(1,maxn)
    intento=input("Intentalo mi pana: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("Intentalo mi pana: ")
    print "Ahora has acertado prro"

adivino_2()
    
