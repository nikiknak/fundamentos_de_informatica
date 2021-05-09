#5:Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
import re

#creamos nuevo archivo
nuevo = open('nuevo_archivo.txt', 'w')

#copiamos la info del viejo en el nuevo
with open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/nuevo_archivo.txt", "w") as f1:
        for line in f:
            f1.write(line)
#modificamos la info
nuevo = open("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/nuevo_archivo.txt", "r+")


nuevotext = nuevo.read()

nuevotext = nuevotext.replace('p', 'p\n')


with open('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/nuevo_archivo.txt', 'w') as file:
  file.write(nuevotext)
