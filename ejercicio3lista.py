# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media,
la nota más alta que ha sacado y la menor.
'''

def lista_notas():
    lst1=[]
    notas=0
    while(notas<5):
        cadena=float(input("Dime tu nota: "))
        if(notas<=10):
            lst1.append(cadena)
            notas +=1
        else:
            print ("La nota",cadena,"no es correcta.")
        
    return lst1

        
#Realizo la media        
lst1=lista_notas()
def media():
    res=0
    for i in lst1:
        res=res+i
        media=res/5
        
    return media

print("Sus notas son:",lst1)

print("La nota media es:",media())

#Busco la nota más alta

def notaMasAlta(lst):
    return max (lst)

def notaMasBaja(lst):
    return min(lst)
    
print("Su nota más alta es:",notaMasAlta(lst1))

print("Su nota más baja es:", notaMasBaja(lst1))
        
