#Ejercicio 7
#Creá un programa que dado un diccionario y una lista añada está última al DataFrame generado a partir del diccionario.
import pandas as pd
dic1 = {"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}
df=pd.DataFrame(data=dic1)
Lista = [1,2,3,4,5,6]
result=df.append(Lista, ignore_index=True, sort=False) 
print(result)
