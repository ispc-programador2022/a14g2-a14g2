#Construir una aplicacion que debe llamar a funciones, cada una en su archivo .py a saber:
# Funcion que muestre cartel de presentacion
# Funcion ing2i, debe permitir el ingreso de 2 valores enteros
# Funcion ing2s, debe permitir el ingreso de 2 valores de tipo string

#1- función suma, retorna la suma de 2 parámetros.
#2-	función resta, retorna la resta de 2 parámetros.
#3-	función producto, retorna el producto de 2 parámetros.
#4-	función cociente, retorna el cociente de 2 parámetros.
#5-	función módulo, retorna el módulo de 2 parámetros.
#6-	función potencia, retorna la potencia del primero elevado al segundo parámetros.
#7-	función radicación, retorna la raiz del primero respecto del segundo parámetros.
#8- No hace nada
# 9- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.
#10- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando lasfunciones anteriores.
#11- función p1, retorna la resta de los 2 primero por el 3er parámetros, usando las funcionesanteriores.
#NO USAR NUMPY
#12- función genrnd que retorna una lista con 50 números aleatorios.
#13- función que devuelva la suma de las combinaciones posibles de los números generadospor la función genrnd tomados de a dos.
#14- función que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos.
#15- función que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos.
#16- función que calcule la media del vector obtenido en genrnd.
#17- función que calcule la mediana del vector obtenido en genrnd.18- función que calcule el rango del vector obtenido en genrnd.
#19- función que calcule la varianza del vector obtenido en genrnd.
#20- función que calcule devuelva el mínimo del vector obtenido en genrnd.
#21- función que calcule devuelva el máximo del vector obtenido en genrnd.
#22- función super_gen genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.
#23- función media_sup que calcule la media del vector obtenido en super_gen.
#24- función mediana_sup que calcule la mediana del vector obtenido en super_gen.
#25- función rango_sup que calcule el rango del vector obtenido en super_gen.
#26- función var_sup que calcule la varianza del vector obtenido en super_gen.
#27- función min_sup que calcule devuelva el mínimo del vector obtenido en super_gen.
#28- función max_sup que calcule devuelva el máximo del vector obtenido en super_gen.
#29- funcion time_16_21 que mida el tiempo de ejecución del 16 al 21
#30- funcion time_22_28 que mida el tiempo de ejecución del 22 al 28

def imprimirAyuda():
    print('1. funcion suma, retorna la suma de 2 parametros')
    print('2. funcion resta, retorna la resta de 2 parametros')
    print('3. funcion producto, retorna el producto de 2 parametros')
    print('4. funcion cociente, retorna el cociente de 2 parametros')
    print('5. funcion modulo, retorna el modulo de 2 parametros')
    print('6. funcion potencia, retorna la potencia de 2 parametros')
    print('7. funcion radicacion, retorna la radicacion de 2 parametros')
    print('8. No hace nada')
    print('9. funcion p1, retorna el producto de los 2 primeros mas el 3er parametro, usando las funciones anteriores')
    print('10. funcion p1, retorna la suma de los 2 primeros mas el 3er parametro, usando las funciones anteriores')    
    print('11. funcion p1, retorna la resta de los 2 primeros mas el 3er parametro, usando las funciones anteriores')
    print('12. funcion genrnd, retorna una lista con 50 numeros aleatorios')
    print('13- función que devuelva la suma de las combinaciones posibles de los números generadospor la función genrnd tomados de a dos. ')
    print('14- funcion que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos. ')
    print('15- funcion que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos. ')
    print('16- funcion que calcule la media del vector obtenido en genrnd. ')
    print('17- funcion que calcule la mediana del vector obtenido en genrnd. ')
    print('18- funcion que calcule el rango del vector obtenido en genrnd. ')
    print('19- funcion que calcule la varianza del vector obtenido en genrnd. ')
    print('20- funcion que calcule devuelva el minimo del vector obtenido en genrnd. ')
    print('21- funcion que calcule devuelva el maximo del vector obtenido en genrnd. ')
    print('22- función super_gen genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.')
    print('23- función media_sup que calcule la media del vector obtenido en super_gen. ')
    print('24- funcion mediana_sup que calcule la mediana del vector obtenido en super_gen. ')
    print('25- funcion rango_sup que calcule el rango del vector obtenido en super_gen. ')
    print('26- funcion var_sup que calcule la varianza del vector obtenido en super_gen. ')
    print('27- funcion min_sup que calcule devuelva el minimo del vector obtenido en super_gen. ')
    print('28- funcion max_sup que calcule devuelva el maximo del vector obtenido en super_gen. ')
    print('29- funcion time_16_21 que mida el tiempo de ejecución del 16 al 21')
    print('30- funcion time_22_28 que mida el tiempo de ejecución del 22 al 28')


#/////////////////////////////////////////////////////////////////////////////////////////////////////
#Funcion ing2i, debe permitir el ingreso de 2 valores enteros
def ing2i():
    try:
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese otro numero: "))
        return a, b
    except ValueError:
        print("Por favor ingrese un numero")
        ing2i()
   

#Funcion ing2s, debe permitir el ingreso de 2 valores de tipo string
def ing2s():
    a = input("Ingrese el primer string: ")
    b = input("Ingrese el segundo string: ")
    return a, b

#Funcion que muestre cartel de presentacion
def presentacion():
    sel= None
    print("Bienvenido al programa de calculo de operaciones")
    a , b = ing2i()
    while(sel not in range(1,31) and (sel !='h' or sel !='H')): 
        print("Por favor ingrese la operacion deseada")
        sel = input("Numerica (1 al 30) o h, para ayuda(h):  ")
        if(sel == 'h' or sel == 'H'):
            return sel, a, b
        elif (int(sel) in range(1,31)):
            return int(sel), a, b
        else:
            print("Por favor ingrese una opcion valida")
            # Tiene que devolver un valor del 1 al 30 o la letra h o H
#/////////////////////////////////////////////////////////////////////////////////////////////////////

# 1-     función suma, retorna la suma de 2 parámetros.
def suma(a,b):
    return a+b

# 2-     función resta, retorna la resta de 2 parámetros.
def resta(a,b):
    return a-b

# 3-     función producto, retorna el producto de 2 parámetros.
def producto(a,b):
    return a*b

# 4-     función cociente, retorna el cociente de 2 parámetros.
def cociente(a,b):
    return a/b

# 5-     función módulo, retorna el módulo de 2 parámetros.
def modulo(a,b):
    return a%b

# 6-     función potencia, retorna la potencia del primero elevado al segundo parámetros.
def potencia(a,b):
    return a**b

#7-     función radicación, retorna la raiz del primero respecto del segundo parámetros.
def radicacion(a,b):
    return a**(1/b)

# 9-     función p1_product, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.
def p1_product(a,b,c):
    return producto(producto(a,b),c)

# 10-     función p1_suma, retorna la suma de los 2 primero por el 3er parámetros, usando lasfunciones anteriores.
def p1_suma(a,b,c):
    return suma(suma(a,b),c)

# 11-     función p1_resta, retorna la resta de los 2 primero por el 3er parámetros, usando las funcionesanteriores.
def p1_resta(a,b,c):
    return resta(resta(a,b),c)

# NO USAR NUMPY
# 12-     función genrnd que retorna una lista con 50 números aleatorios.
def genrnd():
    import random
    lista=[]
    for i in range(50):
        lista.append(random.randint(0,100))
    return lista    

#13-     función suma_gen que devuelva la suma de las combinaciones posibles de los números generadospor la función genrnd tomados de a dos.
def suma_gen():
    lista=genrnd()
    suma=0
    for i in range(50):
        suma+=lista[i]
    return suma 

#14-     función prod_gen que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos.
def prod_gen():
    lista=genrnd()
    prod=1
    for i in range(50):
        prod*=lista[i]
    return prod

#15-     función prod_2gen que devuelva el producto de las combinaciones posibles de los númerosgenerados por la función genrnd tomados de a dos.
def prod_2gen():
    lista=genrnd()
    prod=1
    for i in range(50):
        prod*=lista[i]
    return prod

#16-     función media_gen que calcule la media del vector obtenido en genrnd.
def media_gen():
    lista=genrnd()
    suma=0
    for i in range(50):
        suma+=lista[i]
    return suma/50

#17-     función mediana_gen que calcule la mediana del vector obtenido en genrnd.
def mediana_gen():
    lista=genrnd()
    lista.sort()
    return lista[24]

#18-     función rango_gen que calcule el rango del vector obtenido en genrnd.
def rango_gen():
    lista=genrnd()
    lista.sort()
    return lista[49]-lista[0]

#19-     función var_gen que calcule la varianza del vector obtenido en genrnd.
def var_gen():
    lista=genrnd()
    suma=0
    for i in range(50):
        suma+=lista[i]
    media=suma/50
    suma=0
    for i in range(50):
        suma+=(lista[i]-media)**2
    return suma/50

#20-     función min_gen que calcule devuelva el mínimo del vector obtenido en genrnd.
def min_gen():
    lista=genrnd()
    lista.sort()
    return lista[0]

#21-     función max_gen que calcule devuelva el máximo del vector obtenido en genrnd.
def max_gen():
    lista=genrnd()
    lista.sort()
    return lista[49]

#22-    función super_gen genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.
def super_gen():
    cardin = 500_000_000_000_000_000
    import random
    lista=[]
    for i in range(cardin):
        lista.append(random.randint(0,100))
    return lista

#23      función media_sup que calcule la media del vector obtenido en super_gen.
def media_sup():
    cardin = 500_000_000_000_000_000
    lista=super_gen()
    suma=0
    for i in range(cardin):
        suma+=lista[i]
    return suma/cardin

#24      función mediana_sup que calcule la mediana del vector obtenido en super_gen.
def mediana_sup():
    lista=super_gen()
    lista.sort()
    return lista[24]

#25      función rango_sup que calcule el rango del vector obtenido en super_gen.
def rango_sup():
    lista=super_gen()
    lista.sort()
    return lista[49]-lista[0]

#26      función var_sup que calcule la varianza del vector obtenido en super_gen.
def var_sup():
    cardin = 500_000_000_000_000_000
    lista=super_gen()
    suma=0
    for i in range(cardin):
        suma+=lista[i]
    media=suma/cardin
    suma=0
    for i in range(cardin):
        suma+=(lista[i]-media)**2
    return suma/cardin

#27      función min_sup que calcule devuelva el mínimo del vector obtenido en super_gen.
def min_sup():
    lista=super_gen()
    lista.sort()
    return lista[0]

#28      función max_sup que calcule devuelva el máximo del vector obtenido en super_gen.
def max_sup():
    lista=super_gen()
    lista.sort()
    return lista[49]
    
#29-     función time_16_21 que mida el tiempo de ejecución del 16 al 21
def time_16_21():
    import time
    genrnd()
    start_time=time.time()
    media_gen()
    mediana_gen()
    rango_gen()
    var_gen()
    min_gen()
    max_gen()
    end_time=time.time()
    return end_time-start_time

#30-     funcion time_22_28 que mida el tiempo de ejecución del 22 al 28 
def time_22_28():
    import time
    super_gen()
    start_time=time.time()
    media_sup()
    mediana_sup()
    rango_sup()
    var_sup()
    min_sup()
    max_sup()
    end_time=time.time()
    return end_time-start_time

# Funcion que llama la operacion seleccionada por el usuario, operacion(sel)
def operacion(op):
    if op == 1:
        print(f'La suma entre {a} y {b} es:',suma(a,b))
    elif op == 2:
        print(f'La resta entre {a} y {b} es:',resta(a, b))
    elif op == 3:
        print(f'El producto entre {a} y {b} es:',producto(a, b))
    elif op == 4:
        print(cociente(a, b))
    elif op == 5:
        print(modulo(a, b))
    elif op == 6:
        print(potencia(a, b))
    elif op == 7:
        print(radicacion(a, b))
    elif op == 8:
        print('nada')
    elif op == 9:
        print(p1_product(a,b,c))
    elif op == 10:
        print(p1_suma(a,b,c))
    elif op == 11:
        print(p1_resta(a,b,c))
    elif op == 12:
        print(genrnd())
    elif op == 13:
        print(suma_gen())
    elif op == 14:
        print(prod_gen())
    elif op == 15:
        print(prod_2gen())
    elif op == 16:
        print(media_gen())
    elif op == 17:
        print(mediana_gen())
    elif op == 18:
        print(rango_gen())
    elif op == 19:
        print(var_gen())
    elif op == 20:
        print(min_gen())
    elif op == 21:
        print(max_gen())
    elif op == 22:
        print(super_gen())
    elif op == 23:
        print(media_sup())
    elif op == 24:
        print(mediana_sup())
    elif op == 25:
        print(rango_sup())
    elif op == 26:
        print(var_sup())
    elif op == 27:
        print(min_sup())
    elif op == 28:
        print(max_sup())
    elif op == 29:
        print(time_16_21())
    elif op == 30:
        print(time_22_28())
    else:
        print("Operación no contemplada")


# main() , Funcion principal Inicio del flujo del programa

sel,a,b = presentacion()
while(sel == 'h'):
    imprimirAyuda()
    sel,a,b = presentacion()
else:
    operacion(sel)
    print("Gracias por usar el programa")
    print("Fin del programa")
    print("\n")
# fin_main




