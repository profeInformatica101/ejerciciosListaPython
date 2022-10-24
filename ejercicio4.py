# Ejercicio 4 #
'''
Programa que declare una lista y la vaya llenando de núemros hasta que introducimos un número negativo.
Entonces se debe imprmir el vector (sólo los elementos introducidos)
'''


def ejercicio4():
    lst = []
    while(True):
        try:
            num = float(input("Dime un número: "))
            if(num >= 0):
                lst.append(num)
            else:
                return lst
        except:
            print("Tiene que ser un número")
