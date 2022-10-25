# Ejercicio 7 #
'''
Programa que declare tres listas 'lista1', 'lista2' de cinco enteros cada uno. 
Calcule lista3 = lista1 + lista2, por ejemplo 
           lista1 = [1, 2, 3, 4, 5]
        +  lista2 = [3, 2, 4, 5, 1]
           --------------------------
           lista3 = [4, 4, 7, 9, 6]
           
'''
import random

def listasAleatorias(n):
    lst=[]
    for i in range(0,n):
        lst.append(random.randint(0,10))
    return lst

lst1=listasAleatorias(5)
lst2=listasAleatorias(5)

print(lst1)
print(lst2)

def listaSuma():
    lst3=[]
    
    if(len(lst1)==len(lst2)):
        for i in range (0,len(lst1)):
            lst3.append(lst1[i]+lst2[i])
        
    else:
        print("Tienen que tener el mismo tamaño.")
        
    return lst3

print(listaSuma())
