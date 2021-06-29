#Ejercicio 1
#Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.
#Series de muestra:
#[3, 7, 12, 15, 21], [1, 4, 10, 14, 19]
import pandas as pd
una_serie = pd.Series([3, 7, 12, 15, 21])
otra_serie =pd.Series([1, 4, 10, 14, 19])
print(una_serie + otra_serie)
print(una_serie - otra_serie)
print (una_serie * otra_serie)
print( una_serie / otra_serie)

