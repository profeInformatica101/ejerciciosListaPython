import random
# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''

# Función que crea una lista aleatoria con 10 elementos
def listaAleatoria():
    lst = []
    for i in range(0,10):
        lst.append(random.randint(0,10))
    return lst
# Función que ordena una lista dado una lista
def ordenaLista(lst):
    lst.sort()
    return lst

# Solución ejercicio 5
def ejercicio5():
    lst = listaAleatoria()
    print(ordenaLista(lst))
