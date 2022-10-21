# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''
# Ejercicio 3 #
'''
Se quiere realizar un programa
que lea por teclado las 5 notas
obtenidas por un alumno
(comprendidas entre 0 y 10).
A continuación debe mostrar
todas las notas, la nota media,
la nota más alta que ha sacado y la menor
'''

def ejercicio3():
    #Un listado con 5 notas
    listado = obtenerNotas(5)
    
    #Muestro las notas
    print("Las notas son: ", listado)
    #Muestro la media
    print("La nota media es: ", notaMedia(listado))
    #Muestro la nota más baja
    print("La nota más baja es: ", notaMasBaja(listado))
    #Muestro la nota más alta
    print("La nota más alta es: ", notaMasAlta(listado))

def obtenerNotas(n):
    totalNotas = 0
    lstNotas = []
    while(totalNotas < n):
        try:
            nota = float(input("Dime la nota: "))
            if(nota <= 10):
                lstNotas.append(nota)
                totalNotas += 1
            else:
                print("La nota ", nota , " no es correcta.")
        except:
            print("Tiene que ser un número")
    return lstNotas
    
# Función que realiza la nota media
def notaMedia(lst):
    res = sum(lst) / len(lst)
    return res

# Función que devuelve la nota más baja
def notaMasBaja(lst):
    return min(lst)

# Función que devuelve la nota más alta
def notaMasAlta(lst):
    return max(lst)


##############
# SOLUCION   #
##############
ejercicio3()
