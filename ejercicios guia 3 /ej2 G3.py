#2: Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9]',string))
#  return not bool(re.search('[^a-zA-Z0-9]',string))
#busca cualq caracter que no este aca: a-zA-Z0-9 poniendo: ^
# not me lo convierte en falso osea not bool (no verdadero)
# que no cumpla que a-zA-Z0-9 este en mi string.
print("el string" , "ABCDEFabcdef123450", "tienen todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))
print("el string", "*&@#!}{", "tiene todos los caracteres permitidos?")
print (caracteres_permitidos("*&@#!}{"))
