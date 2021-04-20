#4:Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
from io import open
f= open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt","rt")
mensaje= f.read()
words = mensaje.split()
print("cantidad de palabras en el archivo:", len(words))


 
