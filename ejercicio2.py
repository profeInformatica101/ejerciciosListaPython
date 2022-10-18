# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso,
y muestra sus elementos por la pantalla.
'''
import random

def lista_palabras():
    lst1=[]
    palabras=0
    while(palabras<5):
        cadena = input("Dime una palabra:")
        palabras+=1
        lst1.append(cadena)
        
    return lst1

def ejercicio2():
    lista = lista_palabras()
    lista.reverse()
    return lista
    
