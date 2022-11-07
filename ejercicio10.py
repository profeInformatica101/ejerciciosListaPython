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

print(crearMatriz(5))


        


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
        print("Iteración ", i)
        print(matriz_a[i])
        print(matriz_b[i])
        lst_aux = []
        for j in range(0,len(matriz_a[i])):
            print("matriz_a: ", matriz_a[i][j])
            print("matriz_b: ", matriz_b[i][j])
            suma_aux = matriz_a[i][j] + matriz_b[i][j]
            lst_aux.append(suma_aux)

matriz_a = crearMatriz(5)
matriz_b = crearMatriz(5)

sumaMatrices(matriz_a, matriz_b)

'''
Crea dos matrices y realiza la RESTA
(Tienen que ser matrices equidimiensionales)
    M_A = M_B - M_C
'''

'''
Realiza la Matriz Transpuesta.
Ejemplo

A = [[-3, 7, 5],[1, -2, 3],[2, -12, 4]]
A_T = [[-3, 1, 2],[7, -2,-12],[5, 3, 4]]
