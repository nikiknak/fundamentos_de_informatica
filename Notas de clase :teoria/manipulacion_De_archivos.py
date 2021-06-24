#2. Apertura de archivos

#Para abrir un archivo de texto, ya sea para usarlo o escribir en el, podemos usar la función nativa de Python open():

# open(path_al_archivo, modo) 
# Donde:

# - "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. 

# - "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.

#Modo de apertura	Significado
#r	abre un archivo solo para lectura
#r+	abre un archivo para lectura y escritura
#a	Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura
#w	Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura

# cierre de archivos:
# archivo = open(path_al_archivo, modo) 
# archivo.close()

#Sin embargo, existe otra forma de apertura de archivos que nos ahorra este paso y siempre nos asegura el cierre de adecuado:

#with open(path_al_archivo, modo) as miarch:
    #Aquí van las líneas de procesamiento del archivo

#Este modo de apertura nos asegura el cierre del archivo al salir del bloque with, aún cuando aparezcan errores. Es por eso que esta es la forma más recomendada para la apertura de archivos.

#.read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

#.readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.

#.readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.

#Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
#Para pensar 🤔:¿Cómo darías formato al texto que estas creando?

with open("/Users/niki/Desktop/INFORMATICA/bio.txt", 'a') as file:
    file.write("Me llamo Nicole. \nTengo 19. \nEstoy en mi segundo año de facultad.")
 
texto = open("/Users/niki/Desktop/INFORMATICA/bio.txt",'r')
text = texto.read()
print(text)
texto.close()

bio = open("/Users/niki/Desktop/INFORMATICA/bio.txt",'r')
print(bio.readline())
print(bio.readlines())

import re 
text = open("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/ejericios guia 4/archivo_existente.txt", 'r') #acá estamos haciendo que abra el archivo para que lo pueda leer, pero no lo lee todavía
texto = text.read() #lee el archivo
print(texto)
patron = "-(.*)-"
print("\n")
print(re.search(patron, texto).group())





