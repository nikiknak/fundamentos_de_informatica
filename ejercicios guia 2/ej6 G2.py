#6: Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copiá los elementos de la lista en otra lista pero en orden inverso, 
# imprimí los elementos de esta última lista.
a1 = input("dame un elemento:")
a2 = input("dame un elemento:")
a3 = input("dame un elemento:")
a4 = input("dame un elemento:")
a5 = input("dame un elemento:")
lista=[a1,a2,a3,a4,a5]
#una forma:
#for item in lista [::-1]:
    #print(item)
#otra forma: 
lista2=list(lista)
lista2.reverse()
print(lista2)
