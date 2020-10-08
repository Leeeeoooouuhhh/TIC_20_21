'''Introduce un nombre y un apellido. Genera una contraseña a partir de
3 letras del nombre y 3 del apellido'''
def contrasena_2():
    Nombre=raw_input("Nombre: ")
    Apellido=raw_input("Apellido: ")
    contrasena=Nombre[-3:]+ Apellido[-3:]
    print("contrasena: ",contrasena)
    
contrasena_2()
