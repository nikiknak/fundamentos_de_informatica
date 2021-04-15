#12:Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper():
    contadores[letra] = 0

cadena = input("escribi una cadena: ")

for caracter in cadena:
    if caracter.lower() in alfabeto:
        contadores[caracter]+=1 

for campo, valor in contadores.items():
    print (campo,valor)