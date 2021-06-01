#Ejercicio 3
#Realizá un programa que agregue datos a un DataFrame vacío.
import pandas as pd 
df =pd.DataFrame() # el data frame empiza vacio
df ["nombre"] = ["Nicole", "Martina","Pilar","Sofia"] #agrego una columna
df["apellido"] = ["Knak", "Roch", "Feijoo", "Castaño"] #agrego otra columna
print (df)
