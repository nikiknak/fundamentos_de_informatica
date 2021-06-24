#las secuencias de escape más frecuentes:

#\n	salto de línea
#\t	Tab o cambio de pestaña
#\s	espacio
#'	Comillas simples
#"	Comillas dobles

#Para pensar: ¿Qué usos crees que podemos darle a las expresiones regulares? 
#Proponé una aplicación concreta para tu carrera/disciplina.

#utilizada para describir o encontrar patrones dentro de otros strings
#Se utilizan principalmente para la búsqueda de patrones de cadenas de caracteres u operaciones de sustituciones.
#Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.

#Existen lo que se conoce como metacaracteres delimitadores:
#Metacaracter	Significado
#^	Inicio de línea
#$	Fin de linea
#\A	Inicio de texto
#\Z	Fin de texto
#.	Coincide con cualquier caracter en una línea dada

#Para pensar 🤔: Dado el siguiente texto:

texto = 'Esta es la linea uno\npalabra en la linea dos\n'
print(texto)
#Esta es la linea uno
#palabra en la linea dos

#¿Cómo crees que darán las siguientes búsquedas?

#expresion regular a: '^palabra' --> true (inicio de linea)

#expresion regular b: '\Apalabra' --> false (inicio de texto)
 
#expresion regular c: 'palabra$' --> false (fin de linea)

#expresion regular d: 'palabra\Z' --> false (fin de)


#metacaracteres cuantificadores:

#Metacaracter	Significado
#*	Cero o más: todas las ocurrencias de un dado substring
#+	Una o más ocurrencias del patrón
#?	Cero o una
#{n}	Exactamente n veces
#{n,m}	Por lo menos n pero no más de m veces.


#Para pensar 🤔: ¿Qué significará la expresión regular "X(.*)Y"? Ennumera algunas de las posibles strings que cumplen con dicha condición.
# algo que empiece con X mayuscula y termine Y mayuscula.
#Obtengo lo que se emcuentra entre esas dos letras mas esas letras incluidas.

# Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

# Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

# Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?

#Desafio I: \d{4,}

#Desafio II: [a-z]{3,6}

#Desafio III: ab*

#Para pensar 🤔: ¿Existe una única respuesta para los ejercicios? 
#¿Qué otras alternativas se te ocurren?
# hay varias alternativas
# ejemplo: Xhola123Y

#Los dígitos entre llaves de la forma {n,m}, especifican el mínimo número de ocurrencias en n y el máximo en m.

#Existen tambien metacaracteres predefinidos, que nos facilitan el uso de las expresiones regulares:

#Metacaracter	Significado
#\w	Caracter alfanumércio
#\W	Caracter NO alfanumércio
#\d	Caracter numércio
#\D	Caracter NO numércio
#\s	Un espacio, de cualquier tipo (\t\n\r\f)
#\S	Cualquier caracter que no sea un espacio

#Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
texto = 'En la clase de Introducción a la programación hay 30 estudiantes'
print(texto)
#Desafío IV: /d+


#Rangos

#Un rango es una clase de caracteres abreviada que se crea escribiendo el primer caracter del rango, un guión y el último caracter del rango. Sirve para listar un conjunto de caracteres de interés, de este modo se encontrará uno cualquiera de los caracteres de la lista. Por ejemplo:

#- El rango [a-d] equivale al [abcd]
#- El rango [1-10] equivale al substring [12345678910]
#- El rango [Dd] equivale a buscar una D mayúscula y una d minúscula

#Para trabajar con expresiones regulares en Python, es necesaria la librería RE, que puede ser instalada usando el instalador de Python (PIP):
#pip install re
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto))
#<re.Match object; span=(22, 26), match='amet'>
#span me dice donde esta el substring en todo el texto.
#Si ponemos texto[22:26] nos devuelve amet

# veamos qué hace match():

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.match(patron, texto))
#none
#¿Qué resultado obtenemos con search()?¿Qué diferencias observan con match()?
# La función match() 
#devuelve la primera aparicion y solo al principio de la cadena.
#Si se encuentra  en la primera linea --> devuelve la coincidencia
#si es otra linea --> devuelve Nulo 
# La funcion search()
#nos indica si hizo match, en que posicion se encuentra.

#Comentarios
#El función match() de re busca el patrón y devuelve la primera aparición y solo al principio de la cadena.
#Si se encuentra una coincidencia en la primera línea, devuelve el objeto de coincidencia.
#Pero, si se encuentra una coincidencia en alguna otra línea, devulve un valor nulo.

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group())
#¿Qué resultado obtenemos? ¿Para qué sirve la función group()?
#group() → para  obtener el string de ese search , convertir el objeto a un string.

print(re.findall(patron, texto))
#¿Qué resultado obtenemos?
#['amet', 'amet'] --> devuelve todas las coincidencias en formato lista.

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group())
#amet
print(re.search(patron, texto).group(0))
#amet

#El método group() (o group(0)) nos devuelve la coincidencia.
#Sin embargo si lo que se quiere no es encontrar un patrón en particular,
#sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas palabras) hay que modificar el patrón.
# Vamos a ver el siguiente ejemplo:

import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
print(re.search(patron, texto).group())
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print(re.search(patron, texto).group(0))
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print(re.search(patron, texto).group(1)) # --> → si nos queremos quedar con el substring contenido entre ipsum y sit , sin ipsum y sin sit
#' dolor sit amet, consectetur ipsum elit. Amet '

#Acá se utilizaron algunos metacaracteres, como lo son el punto (.)
#para indicar que puede ser cualquier carácter, y el asterísco (*) para indicar que puede haber 0 o más de estos caracteres.
#De esta manera obtenemos como resultado lo que se encuentre entre las palabras "ipsum" y "sit",
#sin embargo observen dos cosas.
#Primero, el string que nos devuelve tiene dentro un substring que debería haber sido encontrado en la búsqueda: "ipsum dolor sit",
#pero que sin embargo no aparece.
#Segundo, nuevamente al hacer group() o group(0) obtenemos la coincidencia,
#pero si nos queremos quedar con el substring que está contenido entre estas palabras debemos utilizar group(1).
#Ahora bien, como vimos, usar el patrón de búsqueda de esta manera prioriza los matches externos, es decir, busca el primer delimitador ("ipsum" en nuestro caso) y luego abarca todo hasta la última aparición del segundo delimitador ("sit").
#Existe una forma de priorizar los matches internos y es con el metacarácter ?:


texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
print(re.search(patron, texto).group())
#'ipsum dolor sit'
print(re.search(patron, texto).group(0))
#'ipsum dolor sit'
print(re.search(patron, texto).group(1))
#' dolor '

#Cuando se quieren obtener todas las apariciones del patrón se utiliza el método findall el cual actúa para cada coincidencia como si devolviera el group(1),
# es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores.


texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
print(re.findall(patron, texto))
#[' dolor ', ' elit. Amet ']


#Ejecutemos ahora la siguiente línea:

print(re.sub(patron, "###", texto))
# Lorem ### amet, consectetur ### amet.
#Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función sub?
#La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.