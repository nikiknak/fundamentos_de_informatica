#Ejercicio 1
#Escribí un programa de python que imprima un diccionario cuyas claves sean los números de 1 a 15 y cuyos valores sean las potencias al cuadrado de estos números.

diccionario = {}
for numero in range (1,16):
    diccionario[numero]= numero **2
for clave, valor in diccionario.items():
    print(clave,valor)