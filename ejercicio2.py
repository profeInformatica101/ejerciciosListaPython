# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
'''

# Una función que pida por teclado 5 cadena de caracteres
def pedirCadenasCaracteres(n):
   lst = []
   for i in range(0, n):
        cadena = input("Dime una palabra: ")
        lst.append(cadena)
    return lst

def pedirCadenasCaracteres():
    return pedirCadenasCaracteres(5)
    
    
def ejercicio2():
    lista = pedirCadenasCaracteres()
    lista.reverse()
    for i in lista:
        print(i)
