#10: Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
import glob
import os
os.chdir(r"/Users/niki/Desktop/INFORMATICA/Fun. de informatica/GUIAS/ejericios guia 4")
print(os.getcwd())
files_list = glob.glob("*.txt")
print(files_list)
with open(r"Nuevo.txt", "a") as f:
    for file in files_list:
        with open(file, "r") as g:
            f.write(g.read())