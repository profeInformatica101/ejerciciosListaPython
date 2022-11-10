import random
# Ejercicio 10 #
'''
Crear un programa que cree un matriz de 5 x 5
con números aleatorios
'''
# Función que crea un vector con N números aleatorios
def crearVector(n):
    vect = []
    for i in range(0,n):
        vect.append(random.randint(0,20))
    return vect
# Función que crea una Matriz cuadrada de N elementos
def crearMatriz(n):
    matriz = []
    for i in range(0, n):
        matriz.append(crearVector(n))
    return matriz

#print(crearMatriz(5))

      
'''
Crea dos matrices y realiza la SUMA
(Tienen que ser matrices equidimensionales)
    M_A = M_B + M_C
'''
def sumaMatrices(matriz_a, matriz_b):
    matriz_suma = []
    print("A:")
    print(matriz_a)
    print("B:")
    print(matriz_b)
    
    for i in range(0,len(matriz_a)):
        #print("Iteración ", i)
        #print(matriz_a[i])
        #print(matriz_b[i])
        lst_aux = []
        for j in range(0,len(matriz_a[i])):
            #print("matriz_a: ", matriz_a[i][j])
            #print("matriz_b: ", matriz_b[i][j])
            suma_aux = matriz_a[i][j] + matriz_b[i][j]
            lst_aux.append(suma_aux)
        matriz_suma.append(lst_aux)
    return matriz_suma
matriz_a = crearMatriz(5)
matriz_b = crearMatriz(5)

#print(sumaMatrices(matriz_a, matriz_b))

'''
Crea dos matrices y realiza la RESTA
(Tienen que ser matrices equidimiensionales)
    M_A = M_B - M_C
'''
def restaMatrices(matriz_a, matriz_b):
    '''matriz_suma = []
    print("A:")
    print(matriz_a)
    print("B:")
    print(matriz_b)
    '''
    for i in range(0,len(matriz_a)):
        #print("Iteración ", i)
        #print(matriz_a[i])
        #print(matriz_b[i])
        lst_aux = []
        for j in range(0,len(matriz_a[i])):
            #print("matriz_a: ", matriz_a[i][j])
            #print("matriz_b: ", matriz_b[i][j])
            suma_aux = matriz_a[i][j] - matriz_b[i][j]
            lst_aux.append(suma_aux)
        matriz_suma.append(lst_aux)
    return matriz_suma
matriz_a = crearMatriz(5)
matriz_b = crearMatriz(5)

'''
Producto de un número por una MATRIZ

5 x [[1,2,3],[4,5,6],[7,8,9]] = [[5, 10, 15],[20, 25, 30],[35, 40, 45]]

'''
def productoNumeromatriz(matriz):
    producto = int(input("Dime el producto: "))
    matriz_producto = []
    for i in range(0,len(matriz)):
        lst_producto = []
        for x in range(0, len(matriz[i])):
            total = producto * matriz[i][x]
            lst_producto.append(total)
        matriz_producto.append(lst_producto)
    return matriz_producto
    
#matriz_random = crearMatriz(3)
#print(matriz_random)
#print(productoNumeromatriz(matriz_random))


'''Realiza la Matriz Transpuesta.
Ejemplo

A = [[-3, 7, 5],[1, -2, 3],[2, -12, 4]]
A_T = [[-3, 1, 2],[7, -2,-12],[5, 3, 4]]
'''


'''
MULTIPLICACIÓN DE MATRICES
'''
matriz_a = [[2,0,1],[3,0,0],[5,1,1]]
matriz_b = [[1,0,1],[1,2,1],[1,1,0]]

'''
Función auxiliar que devuelve una columna dada una posición y una matriz
'''
def obtenerColumnaMatriz(pos, matriz):
    vector = []
    for i in range(0, len(matriz)):
        vector.append(matriz[i][pos])
    return vector

#print(obtenerColumnaMatriz(1, matriz_b)) #devolverá [0,2,1]

def auxVectoresSumaMult(vect1, vect2):
    aux_total = 0
    for i in range(0, len(vect2)):
        aux_total += vect1[i] * vect2[i]
    return aux_total


def sumaTotalVector(vec1):
    res = 0
    for i in vec1:
        res = res + i
    return res

def multMatrices(matriz1, matriz2):
    matriz = []
    for i in matriz1:
        vector = []
        for j in range(0, len(matriz2)):
            vect_aux = obtenerColumnaMatriz(j, matriz2)
            vector.append(auxVectoresSumaMult(i,vect_aux ))
        matriz.append(vector)
    return matriz



