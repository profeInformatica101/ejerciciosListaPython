# Ejercicio 6 #
'''
Crea un programa que pida un número al usuario, un número de mes
(por ejemplo, el 4). 
El programa dirá cuántos días tiene (por ejemplo 30) y el nombre del mes.
Debes usar listas. Nota: En una lista podemos guardar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días
'''
#Guardar lista con los nombres del mes y los días.
lstMes=[['Enero',31],['Febrero',28],['Marzo',31],['Abril',30],['Mayo',31],
     ['Junio',30],['Julio',31],['Agosto',31],['Septiembre',30],['Octobre',31],
     ['Noviembre',30],['Diciembre',31]]


try:
    mes=int(input("Dime un número: "))
    if(0<mes<=12):
        nombre=lstMes[mes-1][0]
        dias= lstMes[mes-1][1]
        print("El nombre del mes es:",nombre)
        print("Tiene",dias,"días.")
    else:
        print("No es válido.")
except:
    print("Tiene que ser un número.")
            
