#1:Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
import re
f= open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","r")
mensaje =f.readlines()
contador = 0
print(mensaje)
for i in mensaje:
    if re.search("^[^M]", i) is not None:
        contador += 1
print(contador)



