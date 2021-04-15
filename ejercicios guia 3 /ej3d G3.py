#d:	si un string dado tiene una h seguida de dos o tres e.
import re
def encontrar_patron(string):
    patron = "he{2,3}"
# tiene que repetir entre dos  o tres "e"
    if re.search(patron, string):
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))
# se encuentra el patron porq el 3 no implica q sea el maximo. entre 2 y 3 al menos 