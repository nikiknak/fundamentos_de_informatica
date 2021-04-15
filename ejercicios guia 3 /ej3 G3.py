#3:Creá un programa que verifique las siguientes condiciones:
#a: si un string dado tiene una h seguida de ninguna o más e. * (indicar q habia cero o mas coincidencias)
#b:	si un string dado tiene una h seguida de una o más e. + (una o mas ocurriencias)
#c:	si un string dado tiene una h seguida de una o más e. ? ( cero o una ocurrencia)


import re
def encontrar_patron(string):
    patron ="he*"
# me dice q despues de un h puede haber cero o mas letras e"
    if re.search(patron, string):
        return "se encontro el patron"
    else: return "No se encontro el patron"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))