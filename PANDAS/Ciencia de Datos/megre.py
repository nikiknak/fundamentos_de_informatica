import pandas  as  pd 
personas = pd.read_csv("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/personas_2011 (1).csv",sep = ";")
conicet = pd.read_csv("/Users/niki/Desktop/fundamentos_de_informatica/fundamentos_de_informatica/bases de datos/ref_categoria_conicet (1).csv",";")

pers = personas [['persona_id','anio', 'categoria_conicet_id']]
# merge hace un tercer data frame 
#Creá un nuevo DataFrame a partir del DataFrame Personas,
# el cual solo tenga las columnas "persona_id", "anio" y "categoria_conicet_id" 
#pers = izquierda
#conicet = derecha
h1 = pd.merge(pers, conicet,how="right", on = "categoria_conicet_id")
#Utiliza como referencia la columna del df de la derecha, por eso es que tiene menos columnas.
#Agrega todos los de la derecha( conicet)+ los que tienen en comun.
h2 = pd.merge(pers, conicet,how="left", on = "categoria_conicet_id") 
#Utiliza como referencia la columna del df de la izquierda.
#Agrega todos los de la izquierda(personas)+ los que tienen en comun.
h3 = pd.merge(pers, conicet,how="outer", on = "categoria_conicet_id") # junta todo  
h4 = pd.merge(pers, conicet,how="inner", on = "categoria_conicet_id") # lo que tienen en comun(no hay nan)
print(h1)
print(h2)
print(h3)
print(h4)

#left_on  y right_on # cuando no 
h5 = pd.merge(pers, conicet, left_on="persona_id", right_on = "categoria_conicet_id")
print(h5)
# se utiliza para relacionar 2 columnas a traves del merge 
# pers y conicet tienen columnas q se llaman igual entonces se las nombra:
# categoria_conicet_id_x , categoria_conicet_id_y 

pers2 = pers[['persona_id','anio']]
print(pers2)
#h6 = pd.merge(pers2, conicet,how = "inner", left_on="persona_id", right_on = "categoria_conicet_descripcion") # da error porq si yo elimino categoria conicet no me va a parecer nada que tenga eso.
# hay que utilizar merge para columnas del mismo tipo.
 
#left_on  y right_on # cuando no 
h5 = pd.merge(pers, conicet, left_on="persona_id", right_on = "categoria_conicet_id")
print(h5)
# se utiliza para relacionar 2 columnas a traves del merge 
# pers y conicet tienen columnas q se llaman igual entonces se las nombra:
# categoria_conicet_id_x , categoria_conicet_id_y 

pers2 = pers[['persona_id','anio']]
print(pers2)
#h6 = pd.merge(pers2, conicet,how = "inner", left_on="persona_id", right_on = "categoria_conicet_descripcion") # da error porq si yo elimino categoria conicet no me va a parecer nada que tenga eso.
# hay que utilizar merge para columnas del mismo tipo.
 

# 3 METODOS:
 
#1: SET_INDEX 
# pd.set_index()

df = pd.DataFrame({'mes': [1, 4, 7, 10], 'anio': [2012, 2014, 2013, 2014], 'venta': [55, 40, 84, 31]})
print(df)
print(df.set_index('anio'))# Podemos crear múltiples índices
print(df.set_index(['anio', 'mes']))

#2: SORT_VALUES
#pd.df.sort_values()

#ordena los valores de un data frame. Este orden se puede hacer tanto por columnas como por filas, 
#ascendente o descendente, y eligiendo dónde deben ir los NaN.

#axis: por defecto es 0. Con esto elegimos si se ordenan las columnas o las filas.

#ascending: por defecto es True, por lo que se ordena de menor a mayor. Si es False se invierte el orden.

#na_position: por defecto es "last", por lo que todos los valores NaN se ordenan al final, pero se puede configurar como "first" para que aparezcan primero.

df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']})
print(df)

# Ordenamos por columna 1:
print(df.sort_values(by=['col1']))

# Se pueden ordenar por más de una columna a la vez:
print(df.sort_values(by=['col1', 'col2']))

# Ordenamos de forma descenciente y con los NaN al principio:
print(df.sort_values(by='col1', ascending=False, na_position='first'))


#3: TO_CSV
# pd.df.to_csv
#Con este método podemos guardar un data frame en un archivo csv (separado por comas).

#path_or_buf: por defecto es None, por lo que si no le damos una ruta donde debe ser guardado nos va a devolver un string. La ruta puede ser completa o relativa.

#sep: por defecto el separador es una coma, pero igual que con la apertura, este se puede definir.

#na_rep: es la representación de los valores NaN, que por defecto es un string vacío, "", pero también puede ser configurado.

#header: por defecto es True, guarda el archivo con los nombres de las columnas.

#index: idem a header. Cuando los nombres de los índices son generados automáticamente (del 0 en adelante) es mejor que este parámetro tome el valor False.

#EJERCICIO:
# Obtener las 10 personas con mayor edad y generar un nuevo DataFrame con la información de el id de la persona,
# el año, su edad y las producciones académicas de los últimos 4 años. Unirlo con el DataFrame conicet y
# en base a ese generar una tabla con el id de la persona y la descripción de la categoría en conicet. 
# Luego guardar este último DataFrame en un archivo.

