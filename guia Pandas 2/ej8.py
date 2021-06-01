#Ejercicio 8
#Realizá un programa que dado dos DataFrames genere otro que contenga solo las columnas en común.
import pandas as pd
dic1={"FRUTAS":["Banana","Manzana","Melon","Frutilla"], "COMIDAS":["empanada", "pizza","ensalada","papas"]}
dic2={"FRUTAS":["Pomelo", "Durazno","Frutilla", "Melon"], "COMIDAS": ["empanada","asado","tacos","pizza"],"POSTRE": ["helado","flan","volcan ","panqueques"]}
df1 = pd.DataFrame (data=dic1, index = [1,2,3,4])
df2 = pd.DataFrame (data=dic2, index = [1,2,3,4])
print(df1)
print("\n")
print(df2)
print("\n")
result = pd.concat([df1, df2], join="inner") #me devuelve las columnas que tienen en comun los dos dataframes
print(result)
