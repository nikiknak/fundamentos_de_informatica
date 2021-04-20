#6: Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
import re

#creamos nuevo archivo
nuevo = open('nuevo_archivo2.txt', 'w')

#copiamos la info del viejo en el nuevo
with open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/niki/Desktop/nuevo_archivo2.txt", "w") as f1:
        for line in f:
            f1.write(line)

#modificamos la info
tercero = open("/Users/niki/Desktop/nuevo_archivo2.txt", "r+")


tercerotext = tercero.read()

tercerotext = tercerotext.replace('\n',' ')

with open('/Users/niki/Desktop/nuevo_archivo2.txt', 'w') as file:
  file.write(tercerotext)