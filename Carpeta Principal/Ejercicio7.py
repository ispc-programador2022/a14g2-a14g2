'''
Funcion Radicacion, devuelve la raiz del primer respecto del segundo parametro
usando la funcion pow()
'''

def radicacion(x,y):
    z=pow(x,1/y)
    return z

#ejemplo
x=int(input("Ingrese un valor de x: "))
y=int(input("Ingrese un valor de y: "))
print(radicacion(x,y))
