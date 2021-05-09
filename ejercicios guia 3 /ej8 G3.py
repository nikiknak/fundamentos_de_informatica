#8: Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
string = "Hola24576*`"
patron = "\d"
lista = re.findall(patron, string)
for i in lista:
    print(int(i))