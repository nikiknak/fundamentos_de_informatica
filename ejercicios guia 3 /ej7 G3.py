#7: Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
import re 
string = input("Ingrese un texto:")
def letras_numeros_espacios(string):
    return not bool(re.search('[^(a-zA-Z0-9(\s))]',string)) #Si alguno de los caracteres del string no cumple con esta condicion, esto me da verdadero
if letras_numeros_espacios(string):
    print("Este string contiene solamente letras minusculas, mayusculas, espacios o numeros")
else:
    print("Este string no contiene solamente letras minusculas, mayusculas, espacios o numeros")

