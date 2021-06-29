import pandas as pd
una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
print(una_serie)
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
print(paises_latam)
