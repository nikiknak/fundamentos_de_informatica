#11. Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
"""contadores = {} #hago diccionario
cadena = input("Escribi una cadena:")

for caracter in cadena: 
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1
print(contadores)

for llave, valor in contadores.items():
    print(llave, valor)"""

contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper():
    contadores[letra] = 0  
cadena = input("Escribi una cadena:")

for caracter in cadena:
    if caracter.lower() in alfabeto: 
        contadores[caracter]+=1

for campo, valor in contadores.items():
    print(campo, valor)