#Ejercicio 2
#Escribí un programa que guarde en una lista una columna de un DataFrame.
import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
print(df[2].tolist()) #convierte un dataframe en una lista, en este caso agarro la coluna numero 2 y la trasnformo en lista.
