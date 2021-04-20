#2: Escribí un programa que lea un archivo e imprima las primeras n líneas.
import re
f= open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","r")
n = 0
while n <= 5: 
    n += 1
mensaje=f.readline()
print(mensaje)