# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
'''


# Una función que pida por teclado n veces cadena de caracteres y devuelve una lista
def pedirCadenasCaracteres(n):
   lst = []
   for i in range(0, n):
        cadena = input("Dime una palabra: ")
        lst.append(cadena)
   return lst


def ejercicio2():
    lista = pedirCadenasCaracteres(5)
    
    # Copia los elementos de la lista en otra lista 
    lst_reverse =  lista.copy()
    
    #En orden inverso
    lst_reverse.reverse()
    
    #Mostramos sus elementos por pantalla
    for i in lst_reverse:
        print(i)

ejercicio2()
