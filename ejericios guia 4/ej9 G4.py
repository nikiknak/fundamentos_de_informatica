#9: Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
import re

with open(r'/Users/niki/Desktop/INFORMATICA/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt', "r") as texto:
    text = texto.read()
    palabras = text.split()
    print(len(palabras))

    lista_palabras_unicas = []
    for i in palabras:
        if i not in lista_palabras_unicas:
            lista_palabras_unicas.append(i)

    print(lista_palabras_unicas)
    

    for i in lista_palabras_unicas:
        print(re.findall(i, text))
        repeticiones =len(re.findall(i, text))
        frecuencia = float('{:.4f}'.format(repeticiones / len(palabras)))
        print("La frecuencia de " + "'" +str(i) +"'"+ " es: " + str(frecuencia))
