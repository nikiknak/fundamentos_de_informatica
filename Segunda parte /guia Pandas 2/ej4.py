#Ejercicio 4
#Escribí un programa que elimine las primeras n filas de un DataFrame. Pista: el DataFrame original no debe modificarse.
import pandas as pd 
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
print(paises_latam)
df1 = paises_latam.loc[3:] # me devuelve de las 3 para abajo, "eliminando" las filas 0,1,2
print(df1)
