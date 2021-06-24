print('¡Hola terricolas!')
print(3*5) #multiplico
print(8/4) # divido

#Operación	Operador												
#Suma	+												
#División	/												
#Multiplicación	*												
#Exponencial	**

#variable = valor de la variable

#Operación	Operador												
#Igualdad	==												
#Distinto	!=												
#Mayor	>												
#Menor	<

edad_lola = 13
edad_ana = 32
print(edad_lola == edad_ana) #devuelve False 

cadena = "este es un ejemplo de cadena"
print(cadena)

#Las cadenas pueden ser comparadas con los operadores relacionales que vimos antes. Así, podemos saber entonces si son o no son distintas:

afirmacion = "si"
gran_afirmacion = "SI"
print(gran_afirmacion == afirmacion)
# devuelve false porque un si esta en mayuscula y el otro en minuscula entonces no son iguales.

#posiciones:
saludo = "Hola mundo"
print(saludo[0])
# H posicion 0
# H --> 0
# o  --> 1
# l --> 2
# a --> 3

saludo = "Hola mundo"
print(saludo[0:3])
# devuelve Hol ( el cero incluido y el 3 no inculido ( posiciones))

print(saludo[0:]) # imprime todo. 


saludo = "Hola mundo"
print(len(saludo)) # cantidad de caracteres
print(saludo.upper())  # todo en mayuscula
print(saludo.lower()) # tooo en minuscula
print(saludo.count('o')) # poscion de o
print(saludo.replace('o','a')) # remplazo donde hay una "o" una "a"

#Cuando trabajamos con strings también puede resultarnos útil saber si uno contiene a otro, para ello utilizamos el operador in:
print("mar" in "marinero") # true

lista = [2,5,4]
print(lista[0]) # elemento en posicion 0 --> 2

#¿Cómo podrías conocer la longitud de la lista?
print(len(lista)) # 3
print(lista.append('25')) # agrega un elemento
#print(lista.remove('25')) # saca un elemento
print(lista.index('25')) #  me devuelve la posicion de el elemento 25 --> 3

diccionario = {"llave": "valor"}
print(diccionario["llave"]) # acedo al los valores de una llave en particular
print(diccionario.keys()) # me devuelve todas las llaves que se encuentran en un diccionario
print(diccionario.values())# me devuelve todos los valores que se encuentran en un diccionario


#def funcion(argumento):
#    Operación sobre el argumento
#    return aquí va el resultado quiero devolver

def doble(numero):
    resultado = numero * 2
    return resultado

"""Desafío VI: Después de tanto programar necesitamos unos matecitos.
Hoy aprendiste a prepararlos.
Lo que no estoy segura es de que el agua alcance para toda la ronda. 
Suponiendo que cada cebada de mate consume del 30 ml de agua. 
Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos consumiremos para un ronda dada 
(es decir una cantidad de personas dada)."""

def mate(personas):
    agua = (personas * 30)
    resultado = agua / 1000
    if resultado < 1: #si necesito menos de 1l lleno 1 termo
        return 1
    else:
        if agua%1000 == 0:
            return int(resultado) 
        if agua%1000 != 0:
            return int(resultado) + 1

print(mate(20)) #menos de 1000ml (600ml en este caso, y necesita 1 termo)
print(mate(100)) #+ de 1000ml y llena termo completo (3000ml, necesita 3 termos)
print(mate(150)) #+ de 1000ml y queda un termo no completo(4500ml, necesita 5 termos y no usa todo el quinto entero)

def vaquita(costos, comensales):
   return costos / comensales
print(vaquita(100,10))


# if condición:
#    aquí van las órdenes que se ejecutan si la condición es cierta
#  else:
#    aquí van las órdenes que se ejecutan si la condición es falsa

#Como verás una sentencia if se compone de un if, que significa “si”, seguido de una ’condición’ y
#terminando con dos puntos (:). Una condición es un cálculo de programación cuyo resultado es verdadero (True) o falso (False),
#y se crea utilizando los operadores relacionales que ya conocés (==, >, <, !=).


#Definí una función calcular_cantidad_de_agua que espere una cantidad de personas como argumento y devuelva la cantidad de mililitros con los que tenemos que cargar el termo. ¡OJO! Si llega a 1000 debería retornar la advertencia "vas a necesitar más de un térmo"
#línea siguiente son las órdenes a ejecutar si la condición es cierta, y siempre comienza con un tab.
 
def calcular_cantidad_agua(personas): 
    litros_tot = (personas * 30) 
    resultado = litros_tot / 1000
    if resultado < 1:
        return "Llenar un termo con " + str(litros_tot) + "ml" 
    else:
        print("Vas a necesitar mas de un termo") 
        if litros_tot%1000 == 0:
            return "Llenar " + str(int(resultado)) + " termos de 1000ml completos" 
        else:
            sobrante = litros_tot%1000
            return "Llenar " + str(int(resultado)) + " termos completos y uno con " + str(sobrante) + "ml."
print(calcular_cantidad_agua(20)) 
print("\n") 
print(calcular_cantidad_agua(100)) 
print("\n") 
print(calcular_cantidad_agua(150))

# DICCIONARIOS:
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
print(pedido["Ana"]) #no veggie
print(pedido.keys()) #dict_keys(['Ana', 'Paul', 'Luz'])

#Obtenemos la lista de comensales
lista_comensales = pedido.keys()
def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])
empanadas_por_gusto()
#no veggie
#veganas
#vegetarianas


"""Como ya te habrás dado cuenta, el procedimiento que acabamos de crear tiene un bucle ‘for’,
que consiste en un for, una variable cambiante (en nuestro caso i),
un in y una lista de cosas que van a ser los valores que tomará nuestra variable i.
Entonces, nuestro bucle puede ser leído como: para la variable i, tomando valores de la lista lista_comensales
imprimí en la pantalla cada valor del diccionario pedidos que se corresponda a dicha llave."""

#Ahora solo nos faltaría sumar +1 a la lista veggies si el valor es "veganas" o
#sumar +1 a la lista no_veggies si el valor se corresponde con "no veggie"... ¡Pero eso te toca vos!


#Desafío IX: Modificá la función empanadas_por_gusto() para que devuelva la cantidad de empenadas de cada gusto que deben pedirse a la casa de comidas

def empanadas_por_gusto():
    cantidad_veggies= 0
    cantidad_no_veggie = 0
    for i in lista_comensales:
        if pedido[i] == "veganas":
            print(pedido[i]+" "+str(cantidad_veggies+ 1))
        else:
             print(pedido[i]+" "+str(cantidad_no_veggie + 1))
empanadas_por_gusto()
#no veggie 1
#veganas 1
#vegetarianas 1

