#how: indica la manera de unión de los data frames, por defecto es “inner” (intersección).

#on: indica en base a qué columna se van a unir los data frames. Esta columna tiene que estar presente en ambos data frames.

#left_on: nombre de la columna de los datos de la izquierda el cual se va a usar para unir los data frames.

#right_on: igual al anterior, pero con una columna de los datos de la derecha. Ambos tienen que explicitarse.


#inner --> es por defecto siempre
# inner me devuelve lo que comparten dos datafrmes
import pandas as pd 
df1 = pd.DataFrame({"city":["new york", "chicago", "orlando", "baltimore"], "temperature": [21,14,35,32]})
print(df1)
#       city        temperature
# 0   new york           21
# 1    chicago           14
# 2    orlando           35
# 3  baltimore           32

df2 = pd.DataFrame({"city":["chicago", "new york", "san franciso"], "temperature": [65,68,71]})
print(df2)
#       city       temperature
# 0    chicago           65
# 1   new york           68
# 2  san franciso        71

df3 =pd.merge(df1, df2, on= "city") 
#me hace un merge (inner es por defecto siempre,entonces no es necesario ponerlo) 
#y me trae las coincidencias que hay en la columna "city"
print(df3)
#       city   temperature_x  temperature_y
# 0  new york       21             68
# 1   chicago       14             65

#outer me devuelve todo, es la union
df4 =pd.merge(df1, df2,how= "outer", on= "city") 
print(df4)
#  se une en base a la columna city
# hay dos columnas con el mismo nombre entonces a df1 le pone: temperature_x  y a df2 le pone: temperature_y
#           city  temperature_x  temperature_y
# 0      new york           21.0           68.0
# 1       chicago           14.0           65.0
# 2       orlando           35.0            NaN
# 3     baltimore           32.0            NaN
# 4  san franciso            NaN           71.0

df41 =pd.merge(df1, df2,how= "outer") 
print(df41)
# no hay un "on =" entonces me devuelve las dos columnas unidas de los dos data frames.
#           city  temperature
# 0      new york           21
# 1       chicago           14
# 2       orlando           35
# 3     baltimore           32
# 4       chicago           65
# 5      new york           68
# 6  san franciso           71

#---> left es df1
#---> right es df2
#LEFT:
#left me devuelve todo df1 (se encuentra a la izquierda) mas lo que comparte con df2.

df6 =pd.merge(df1, df2,how= "left") 
print(df6) 
# no basandose en la columna city --> me devuelve el dataframe df1.

df6 =pd.merge(df1, df2,how= "left", on = "city") 
print(df6)
# basandose en la columna city me devuelve esto:
#       city     temperature_x  temperature_y
# 0   new york         21           68.0  --> esto lo comparte con df2   *
# 1    chicago         14           65.0  --> esto lo comparte con df2   *
# 2    orlando         35            NaN                                 *    --> todo "*" pertenece a df1
# 3  baltimore         32            NaN                                 *

#RIGHT:
#right me devuelve todo df2 (se encuentra a la derecha) mas lo que comparte con df1.

df7=pd.merge(df1, df2,how= "right") 
print(df7) 
# no basandose en la columna city --> me devuelve el dataframe df2.

df7=pd.merge(df1, df2,how= "right", on = "city") 
print(df7) 
#basandose en la columna city
#         city   temperature_x  temperature_y
# 0       chicago           14.0             65 --> comparte con df1  *
# 1      new york           21.0             68 --> compoarte con df1 *  --> todo "*" pertenece a df2
# 2  san franciso            NaN             71                       * 


df8=pd.merge(df1, df2,how= "outer",  indicator= True ) 
print(df8)
#        city      temperature    _merge
# 0      new york           21   left_only
# 1       chicago           14   left_only
# 2       orlando           35   left_only
# 3     baltimore           32   left_only
# 4       chicago           65  right_only
# 5      new york           68  right_only
# 6  san franciso           71  right_only

df9=pd.merge(df1, df2,how= "outer", on = "city",  indicator= True ) 
print(df9)
#           city  temperature_x  temperature_y      _merge
# 0      new york           21.0           68.0        both
# 1       chicago           14.0           65.0        both
# 2       orlando           35.0            NaN   left_only
# 3     baltimore           32.0            NaN   left_only
# 4  san franciso            NaN           71.0  right_only
