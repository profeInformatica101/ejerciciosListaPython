# Ejercicio 8 #
'''
Denifinir una estructura de datos con listas que permita guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:
     - La temperatura media de cada día
     - Los días con menos temperatura
     - Que permita leer una temperatura por teclado y muestre los días cuya temperatura máxima coincida con ella, en caso contrario mostrar un mensaje diciendo que no existe ningún día
     
'''

import random

def Temperatura():
    lst=[]
    for i in range (0,5):
        min_=random.randint(-30,10)
        max_=random.randint(10,40)
        lst.append([min_ , max_])
    return lst



def temp_media(lst_temp):
    lstMedia=[]
    res=0
    for i in lst_temp:
        res=(i[0]+i[1])/2
        lstMedia.append(res)
    return lstMedia
        


def minTemperatura(lst_temp):
    lstmin=[]
    for i in lst_temp:
        lstmin.append(i[0])
    lstmin.sort()
    return lstmin[0]

def diasminimos(lst_temp):
    mintodos=minTemperatura(lst_temp)
    print(mintodos)
    lstDias=[]
    for i in range(0,len(lst_temp)):
        if (mintodos==lst_temp[i][0]):
            print("test")
            lstDias.append(i+1)
    return lstDias

lst_temp=Temperatura()
print(lst_temp)
print(diasminimos(lst_temp))
