#Ejercicio 4
#Realizá un programa que a partir de una lista mixta 
# (que contiene distintos tipos de datos) 
# imprima cuántos enteros tiene y además en el caso de los
#  elementos que sean strings hay que crear una nueva lista con 
# estos strings pero reemplazando al A por la U (tanto mayúscula como minúscula) 
# y luego imprimir estos elementos.

import re
lista_mixta = ["asd", 23, {"Hola": "Chau"}, 0.211, [1,2,3], 45, 211, "Axx"]
lista = []
enteros = 0

for i in lista_mixta:
     if type(i) == int:
        enteros +=1
     if type(i) == str and ("a" in i or "A" in i): 
          lista.append(i.replace("a", "u").replace("A", "U"))

print(enteros)
print(lista)lista = ["asdsa", "dsasadsa", "asa"]