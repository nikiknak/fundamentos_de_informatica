# Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, 
# que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa 
# tiene que pedir el número de días que se van a introducir.
def temp_media(temp, temp1):
    return (temp + temp1) / 2

dias = int(input("Ingrese la cantidad de dias: "))
num = 0
while num < dias:
    max = float(input("Ingrese la temperatura maxima del dia: "))
    min = float(input("Ingrese la temperatura minima del dia: "))
    num += 1
    print(temp_media(max, min))