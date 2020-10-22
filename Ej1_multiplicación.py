'''Multiplicacion que reciba como argumento 4 numeros reales distintios de 0'''
def multiplicacion():
    acumuladora=1
    print "Introduce un numero: "
    for cont in range(1,5):
        print "Numero ",cont 
        numero=input()
        acumuladora=acumuladora*numero
    print "Producto= ",acumuladora

multiplicacion()
    
        
    
    
