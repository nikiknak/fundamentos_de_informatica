import pandas as pd

una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
print(una_serie)
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
print(paises_latam)

df = pd.read_csv("/Users/niki/Downloads/personas_2011 (2).csv",sep = ";")
##sep: delimitador a usar, indica como separar los elementos.
#Pero en este caso usamos punto y coma porque los datos estan separados por comas ya.

print(df)
print(df.head()) #devuelve las primeras 5 filas
print(df.describe()) #DEVUELVE DATOS ESTADISTICOS (mean, count, max, min etc.) se usa para el analisis de los datos.
print(df.tail()) #devuelve las ultimas 5 filas
print(len(df)) #cantidad de filas 
print(df.info()) #cuantos datos no nulos se encuentran  y que tipos de datos son. Aca son numeros enteros.
#Podemos acceder a los datos de cada columna haciendo

# Header: usa los valores de la primera fila como nombre de columnas
#df = pd.read_csv("/Users/niki/Downloads/personas_2011 (2).csv",sep = ";", header = 1)
#nrows: devuelve las primeras 2 filas
#df = pd.read_csv("/Users/niki/Downloads/personas_2011 (2).csv",sep = ";", nrows=2) 
#index_col: columna/s para usar como los "labels" del DataFrame.

#Para pensar 🤔: ¿Podés imprimir la columna de los max_dedicacion_horaria_docente_id de nuestra tabla? ¿Cómo calcularías el promedio de esta columna?
print(df['max_dedicacion_horaria_docente_id'])
print(df['max_dedicacion_horaria_docente_id'].mean())
#2.284580592105263
# df['nombre de la columna'], en nuestro caso por ejemplo:
print(df['persona_id']) # --> es un objeto 
#me devuelve:  Name: persona_id, Length: 68552, dtype: int64
print(df.loc[2, 'persona_id']) # para saber el dato de una celda en particular #me devuelve: 7 
# me devuelve el Id de la persona que se encuentra en la fila numero 2.
#¿Cómo obtendrías la edad de esa persona?
print(df.loc[2,"edad"]) #la edad que tiene esa persona (persona numero 2, fila 2) es 30.
# acceder a los datos de una columna de un Dataframe como una lista mediante el metodo tolist():
#print(df['edad'].tolist()) #devuelve todas las edades en formato lista.

print(df['edad'].unique())
#Desafío IV: 
# Extrae la columna seniority_level y contá cuántas personas tenían expertice nivel B, C y D
print(df["seniority_level"].count()) #68552
print(df.groupby("seniority_level")) # me devuelve un objeto, es un tipo de objeto que en si es un dataframe
print(df.groupby("seniority_level").count()) #cuantos tipos de seniority_level hay, devolviendo toda la info de cada uno de ellos.
# en este caso esta el A, B, C, D y S/D
#pero para obtener informacion mas exacta: seniority_level y contá cuántas personas tenían expertice nivel B, C y D
#hago:
print(df.groupby("seniority_level")[["persona_id"]].count()) #solo me duevuelve los datos de personn_id teniendo en cuanta seniority_level
# B = 6674, C = 13645 y D = 5774
print(df['edad'] * 2) #me devuelve en numero entero ( se multiplica la edad por 2)
print(df['edad'] + 2) # me devuelve en numero entero ( se le suma a la edad 2)
print(df['edad'] > 2) # me devuelve en bool ( si la edad es mayor a 2 me devuelve true y si es menor me devuelve false, hay algunas personas que tienen edad -1 por eso da false)
print(df[df['edad'] > 35 ]) # me deuvelve los datos de todas las personas con mas de 35 años.


#Desafío V: 
#Contá cuántas personas de 30 años ingresaron al ministerio en 2011 
#¿Cuántas formas de hacer este cálculo se te ocurren?
print(df[df["edad"]== 30]) # cantidad de personas 2098

#base de datos relacionales y no relacionales

print(df['maximo_grado_academico_id'].value_counts())

#Desafío VI: Descargala en formato csv y cargala en un nuevo DataFrame de nombre
categoria= pd.read_csv("/Users/niki/Desktop/INFORMATICA/ref_categoria_conicet (1).csv",";")
print(categoria)

#Desafío VII: Identificá si existen columnas en común con el DataFrame grande

df3 = pd.merge( df, categoria, on='categoria_conicet_id')
print(df3)
#Para pensar 🤔: ¿Qué datos tiene df3? ¿Qué hace el método concat() 
# y qué diferencia tiene con hacer merge()?
df3 = pd.concat([df, categoria,])

# concat: (une dos datos de pandas)
#merge nos permite realizar "joins" entre tablas. El join es realizado sobre las columnas o sobre las filas.

#3. Métodos de los DataFrames

# Lectura/carga de datos:        Limpieza de los datos:	 Estdistica de los datos:
# pd.read_csv()                  pd.head()               pd.describe()
# pd.read_table()                pd.fillna()	         df.sample()
# pd.read_excel()                pd.dropna()             pd.mean()
# pd.read_sql()                  pd.sort_values()        pd.median()
# pd.read_json()                 pd.groupby()            pd.std()
# pd.to_csv()                    pd.apply()              pd.min()
# pd.DataFrame()                 pd.append()             pd.max()
# pd.concat()                    pd.rename()             pd.count()
# pd.Series()                    pd.set_index()          pd.corr()
# pd.DataFrame.from_dict()       pd.tail()               pd.hist()

