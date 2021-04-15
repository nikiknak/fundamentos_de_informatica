#9:Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada 
# alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar 
# se deben mostrar los siguientes datos:
# La edad máxima de todos los alumnos
# Los alumnos que tengan la edad máxima

lista_nombres=[]
lista_edades=[]

nom = input("ingrese un nombre:")
if nom != "*":
    lista_nombres.append(nom)    
    edad =int(input("Ingrese su edad:"))
    lista_edades.append(edad)
else:
    print("No hay alumnos")
while nom != "*": 
    nom = input("ingrese un nombre:")
    if nom != "*":
        lista_nombres.append(nom)
        edad = int(input("ingrese su edad:"))
        lista_edades.append(edad)

edad_max = max(lista_edades)
for i in range(len(lista_edades)):
    if lista_edades[i] == edad_max:
        print(lista_nombres[i])


