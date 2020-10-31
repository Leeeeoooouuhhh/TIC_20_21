'''Precio y un tipo de IVA
General=16%
Reducido=7%
Superreducido=4%
Que devuelva el precio más el IVA'''
def precio_final(num,iva):
    tipos_iva = {
       "general": 0.16,
       "reducido": 0.07,
       "superreducido": 0.04
    }

    iva=num*tipos_iva[iva]
    return num+iva

    
print(precio_final(100,"reducido"))



   
