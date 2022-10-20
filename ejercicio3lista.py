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
        cadena=int(input("Dime tu nota: "))
        notas +=1
        lst1.append(cadena)
        
    return lst1

        
#Realizo la media        
lst1=lista_notas()
def media():
    res=0
    for i in lst1:
        res=res+i
        media=res/5
        
    return media

#print("Sus notas son:",lst1,"La nota media es:",media())
#Busco la nota más alta

def nota_alta_baja():
    for i in lst1:
        alta=0
        baja=11
        contador=0
        while(contadro<5):
            if(alta<i):
                alta=i
                
            if(baja>i):
                baja=i
    
    


    
      

