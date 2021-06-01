#Ejercicio 6
#Escribí un programa que dado dos diccionarios genere dos DataFrame y los una tanto en el eje de las columnas como en el eje de las filas.
import pandas as pd 
dic1= {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
dic2 = {"nombre": ["Nicole", "Martina", "Sofia", "Agustina"],"puntaje":[13,14,6.7,9.5],"intentos": [1, 6, 5, 3],"califica": [1, 0, 1, 1]}
df1=pd.DataFrame(data= dic1)
df2= pd.DataFrame(data=dic2)

columnas =pd.concat([df1,df2],ignore_index=True, sort=False)
print(columnas)
print("\n")
filas= pd.concat([df1, df2], axis=1)
print(filas)