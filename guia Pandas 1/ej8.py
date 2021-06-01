#Ejercicio 8
#Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" 
#del DataFrama anterior.
import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
df = pd.DataFrame (datos_ejemplo)
print(df.groupby("nombre")[["puntaje"]].count())
