import pandas as pd
import seaborn as sns
import scipy.stats as ss
import matplotlib.pyplot as plt
# para hacer un "join" entre tablas se hace esto:
personas11 = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/personas_2011 (1).csv', sep=";")

condicion = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_tipo_condicion_docente.csv', sep = ';')
cargo = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_clase_cargo.csv', sep = ';')
dedicacion = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/.ref_tipo_dedicacion_horaria_semanal.csv.icloud', sep = ';')
categoria = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_categoria_conicet (1).csv', sep = ';')
personal = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_tipo_personal.csv', sep=';')
disciplina = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_disciplina.csv', sep=';')
grado = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_grado_academico.csv', sep=';')
sexo = pd.read_csv('/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_sexo.csv', sep=';')

#personas_cat = pd.merge(personas11, condicion, on = 'tipo_condicion_docente_id')
#personas_cat = pd.merge(personas11, cargo, on = 'clase_cargo_docente_id')
#personas_cat = pd.merge(personas11, dedicacion, on = 'tipo_dedicacion_horaria_semanal_id')
#personas_cat = pd.merge(personas11, categoria, on = 'categoria_conicet_id')
#personas_cat = pd.merge(personas11, personal, on = 'tipo_personal_id')
#personas_cat = pd.merge(personas11, disciplina, on = 'disciplina_id')
#personas_cat = pd.merge(personas11, grado, on = 'grado_academico_id')
#personas_cat = pd.merge(personas11, sexo, on = 'sexo_id')

#print(personas_cat)


# lo hice en un excel directamente y lo llame personas_full
#info : cuantos datos no nulos se encuentran y que tipos de datos son.
#describe: datos estadisticos 
personas_full =pd.read_csv("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/personas_full (1).csv")
print(personas_full)

print(personas_full.describe())
print(personas_full.info())

print(personas_full['grado_academico_id'].value_counts())
# 5    26932
# 1    15075
# 2     7764
# 3     7204
# 7     5271
# -1     5055
# 6     1017
# 8      234
# Name: grado_academico_id, dtype: int64

print(personas_full.isnull())
print(personas_full.isnull().sum()) #cuantas celdas se ecuentran sin informacion valores nulos 


print(sns.heatmap(personas_full.isnull(), cmap='viridis'))  # cada color representa un valor de la fila
#plt.show() # me aparece el grafico en una pestaña nueva.
#plt.savefig('grafico.png') lo grado en esta carpeta

# las columnas con valores nulos son las que se ven en amarillo
# violetas son los datos no nulos 
# los valores Nan son los valores nulos (celdas donde no hay ningun dato)

#Desafío II: Calcular el porcentaje del total de datos, representan los datos nulos de cada columna (variable)
print(personas_full.isnull().sum()/len(personas_full.persona_id) * 100)


#los datos faltantes no me aportan informacion
#Una de las soluciones posibles para el tratamiento de los datos faltantes es la eliminación de casos completos,
#es decir eliminar toda las filas que contienen un dato faltante:
print(personas_full.dropna(inplace=True)) #1: eliminar las filas que le falten datos --> 
print(personas_full.dropna(thresh=2, inplace=True)) # thresh = 2 dice: aquellas filas que tengas 2 datos faltantes eliminalas 

#¿Qué desventajas crees que tiene esta forma de lidiar con los datos faltantes?¿Cuándo lo usarías?
#1: se me achica el espacio muestral
#2: perder datos importantes de otras columnas 
#3: ¿cuando lo uso? Cuando hay pocos Nan (datos faltantes) ya que si hay muchos estoy  eliminando mucha informacion(columnas) que puede llegar a ser importante. 

# Otra solución posible para el tratamiento de datos faltantes sería la eliminación por columna:
print(personas_full.drop(['grado_academico_id'], axis=1, inplace=True))

#Desafío III: Escribí el código que usarías para reemplazar los faltantes por la moda y por la mediana.
#df.fillna(df['columna_con_faltantes'].mode(), inplace=True)
#df.fillna(df['columna_con_faltantes'].median(), inplace=True)
#print(df)
# Distorsiona la verdadera distribución de la variable Distorsiona la correlación entre variables dado que añade valores constantes
print(personas_full.mode())
print(personas_full.median())

#AJUSTE DE TIPOS DE DATOS DE LAS COLUMNAS Y DUPLICADOS:

#En algunos casos las bases de datos suelen tener algunas inconsistencias de tipos de datos, por ejemplo columnas que deberían ser numéricas y se cargan como (strings) 
#o el formato de las fechas es inadecuado. Es por ello que resulta muy importante cerciorarse antes de operar con las columnas, es necesario realizar algunos ajustes en los tipos de datos.

# DTYPES:
#Podemos conocer el tipo de dato al que se corresponde una columna mediante el método dtypes:
#df['columna_de_interes'].dtypes

# TO_NUMERIC:
#Y convertir una columna a tipo de dato numérico, haciendo:
#df['columna_de_interes'] = pd.to_numeric(df['columna_de_interes'], errors='coerce')

#REMOVER DATOS DUPLICADOS:
#Así mismo es frecuente encontrar celdas duplicadas en los datos, que facilmente pueden ser removidos mediante:
#df.drop_duplicates(inplace=True)

#Desafío III: Revisá el DataFrame para detectar otras anomalías en los datos y averiguá como resolverlas.

print (personas_full.drop_duplicates(inplace=True))
