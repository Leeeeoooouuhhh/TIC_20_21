Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def tabla():
	n_tabla=input("Dime la tabla: ")
	print "TABLA DEL ", n_tabla
	for cont in range(1,10):
		print n_tabla," x ",cont," = ",n_tabla*cont

		
>>> tabla()
