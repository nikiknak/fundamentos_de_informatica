#Ejercicio 5
#Realizá un programa que verifique si una columna dada se encuentra presente en un DataFrame.
import pandas as pd 
datos = {"A": [1,2,3,4], "B": [5,6,7,8], "C": [9,10,11,12]}
df=pd.DataFrame(data=datos, index=["w","x","y","z"])
print(df)
verifique = "A" in df.columns
print(verifique)
verifique2 = "a" in df.columns
print(verifique2)
