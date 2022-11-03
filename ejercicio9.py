import random
# Ejercicio 9 #
lst = [0, 1, 3, 5]
def sumaLista(lst):
    sumaTotal = 0
    for i in lst:
        sumaTotal = sumaTotal + i
    return sumaTotal
        
    

'''
Implementar la siguientes funciones 
        - sumaVector(<Lista>) devuelve <Entero>.
        - sumaVectorDeVector(<Lista>) devuelve <Entero>.
        
      
              
'''
def generarListaRandom():
    lst = []
    for i in range(0,random.randint(0,10)):
        lst.append(random.randint(0, 50))
    return lst

def generarListadeListaRandom():
    lst = []
    for i in range(0, random.randint(0,5)):
        lst.append(generarListaRandom())
    return lst

# Dado una lista con números enteros devolver la suma de todos ellos por ejemplo:
              # sumaVector([1,2,3]) -->  6
              # sumaVector([3,4]) --> 7
def sumaVector(lst):
    #print(lst)
    sumaTotal = 0
    for i in range(0, len(lst)):
        #print("i: ", i, "lst[i]:", lst[i])
        sumaTotal = sumaTotal + lst[i]
        #print(sumaTotal)
    return sumaTotal

# Dado una lista con listas de números enteros devolver la suma de todos ellos por ejemplo:
              # sumaVectorDeVector([[1,2],[3,4],[5,6,7]]) --> 28
lst_lst = [[1,2],[3,4],[5,6,7]]

def sumaVectorDeVector(lst):
    resultado = 0
    
    for i in lst:
        resultado = resultado + sumaVector(i)
    
    return resultado
