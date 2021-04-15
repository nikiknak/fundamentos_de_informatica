#1: Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
texto= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron ="[a-zA-Z0-9]"

def programa_verificado(patron,texto):
    if re.search(patron,texto):
        print("verificado")
        
    else:
        print("no verificado")
programa_verificado(patron,texto)

