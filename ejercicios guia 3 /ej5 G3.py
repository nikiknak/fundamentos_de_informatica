#5: Escribí un programa que diga si un string empieza con un número específico.
import re
string= input("Ingrese un string:")
patron= "^4"
if re.search(patron,string) is not None:
    print("el string empieza con el numero 4 ")
else:
    print(" el string no empieza con el numero 4")