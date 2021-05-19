#Ejercicio 3
#Escribí un programa que obtenga,
# a partir de una lista de strings una lista con la longitud de esas strings 
# e imprima la longitud de la lista de strings y los elementos de la lista de longitudes

lista = ["hola","chau"]
listaNueva =[]
for elemento in lista:
    listaNueva.append(len(elemento))
    print("Hay", len(lista), "strings en la lista")
    print("sus longitudes son:")
    for long in listaNueva:
        print(long)
