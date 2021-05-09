#7: Escribí un porgrama que lea un archivo  e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
import re
with  open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as file:
    data=file.read().split()
    max=len(max(data,key=len))
    print(max)
    resultado=[palabra for palabra in data if len(palabra)==max]
    print(resultado)
