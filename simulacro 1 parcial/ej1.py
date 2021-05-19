#Consigna N°1
#Escribir funciones que, dado un String, permitan obtener
#cuántas veces aparece el string abc. P.ej. aparece 2 veces en xcabcb3sabc9, y ninguna en hola amigos mios.
#la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

def cuantas_veces_aparece_abc (cadena, buscar):
	return cadena.count(buscar)
print(cuantas_veces_aparece_abc("xcabcb3sabc9","abc"))
print(cuantas_veces_aparece_abc("hola amigos mios","abc"))
import re
def lista_substrings (cadena, inicio, fin, no_incluir):
	coincidencias =re.findall (inicio +"(.*?)"+ fin, cadena)
	result =[]
	for coincidencia in coincidencias:
		if coincidencia.find (no_incluir) == -1:
			result.append(coincidencia)
			return result
print(lista_substrings("ttaatatggttaacatgg","aa","gg","c"))

