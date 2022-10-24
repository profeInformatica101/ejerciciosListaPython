# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios
(10 valores), y posterior ordene los elementos de menor a mayor.
'''

import random

#Creo una lista con numeros aleatorios.

def lista_aleatorio():
    lst= []
    for i in range(0,10):
        lst.append (random.randint(0,20))
    return lst

#La ordeno de mayor a menor.

lst1=lista_aleatorio()
def lista_orden():
    lst1.sort()
    lst1.reverse
    return lst1

print(lst1)
print(lista_orden())
    
    
        

