Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def suma_gauss():
	n_final=100
	suma_acumulada=0
	for cont in range(1,n_final+1):
		suma_acumulada = suma_acumulada+cont
	print "La suma de los números hasta ", n_final
	print " = ", suma_acumulada

	
>>> suma_gauss()
La suma de los números hasta  100
 =  5050
>>> 
