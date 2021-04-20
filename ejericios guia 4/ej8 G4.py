#8: Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
import re
#copiamos la info del primero en el nuevo (en este caso el poema)
with open("/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/niki/Desktop/otro_archivo.txt", "w") as f1:
        for line in f:
            f1.write(line)

#copiamos la info en otro_archivo (usamos 'a' xq sino lo sobreescribe)
with open("/Users/niki/Desktop/otro_archivo.txt") as f:
    with open("/Users/niki/Desktop/archivo_existente.txt", "a") as f1:
        for line in f:
            f1.write(line)
