# Ejercicio 1 #
'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''

import random

def lst10num():
    lst=[]
    for i in range(0,10):
        lst.append(random.randint(1,10))
    return lst

lst1=lst10num()

for i in lst1:
    res1=i*i
    res2=i*i*i
    print("El cuadrado de",i, "es:" ,res1 ," y el cubo es:",res2)
    
'''    
def cuadrado(x):
    return x*x

def cubo(x):
    return x*x*x

def ejercicio1():
    lista=lst10num()
    
    for i in lista:
        print(i, "cuadrado ->" ,cuadrado(i), "cubo ->", cubo(i) )'''
    
