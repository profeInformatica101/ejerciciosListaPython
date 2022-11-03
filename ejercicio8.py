import random
# Ejercicio 8 #
'''
Definir una estructura de datos con listas que permita guardar
la temperatura mínima y máxima de 5 días.
---
Realiza un programa que de la siguiente información:
     - La temperatura media de cada día
     - Los días con menos temperatura
     - Que permita leer una temperatura por teclado y muestre
       los días cuya temperatura máxima coincida con ella,
       en caso contrario mostrar un mensaje diciendo
       que no existe ningún día
     
'''
# Esto es una función que genera aleatoriamente una de lista de listas con temperaturas minimas y maximas
def listaTemperatura(n):
    lst = []
    for i in range(0,n):
        min_ = random.randint(-30, 10)
        max_ = random.randint(10, 40)
        lst.append([min_, max_])
    return lst

# Función que calcula la temperatura media de cada día
def temperaturaMedia(lista):
    lst_media_temp= []
    for i in lista:
        media = (i[0] + i[1]) /2
        lst_media_temp.append(media)
   
    return lst_media_temp

# Función que calcula los días con menos temperatura
def menosTemperatura(lista):
    lista_minimos= []
    temperatura_minima = lista[0][0]
    for i in lista:
        if(i[0] <= temperatura_minima):
            temperatura_minima = i[0]
    print(temperatura_minima)
    
    for i in range(0,len(lista)):
        if(temperatura_minima == lista[i][0]):

            lista_minimos.append(i+1)
           
    return lista_minimos
''' - Que permita leer una temperatura por teclado
y muestre los días cuya temperatura máxima coincida con ella,
en caso contrario mostrar un mensaje diciendo que no existe
ningún día '''
def buscarTemperaturaMaxima(lista1):
    temp = float(input("Dime la temperatura:"))
    
    lista_dias_max = []
    lista_max = []
    
    for i in lista1:
        #Se agregan todas las temperaturas máximas a una lista vacia
        lista_max.append(i[1])
    
    for i in range(0, len(lista_max)):
        if(lista_max[i] == temp):
            lista_dias_max.append(i+1)
            return lista_dias_max
    else:
        print("No existe ningun día con esa temperatura")
        

lista1= listaTemperatura(5)
lista2= listaTemperatura(10)
lista3= listaTemperatura(0)

