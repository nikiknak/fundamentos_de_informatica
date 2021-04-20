#3: Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
import re
f= open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","r")
mensaje =f.readlines()
print(mensaje[-5:-1])
