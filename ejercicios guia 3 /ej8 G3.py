#8: Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
string = input("Ingrese un texto:")
patron = "\d"
lista = re.findall(patron, string)
for i in lista:
    print(int(i))