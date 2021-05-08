#8: Realizá un programa que declare tres listas lista1, lista2 y lista3,
# donde las dos primeras listas deben tener cinco enteros cada una, 
# ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos 
# de la lista1 y la lista2 
# (es decir, el primer elemento de la lista3 tiene que ser la suma del primer
# elemento de la lista1 y el primero de la lista2)
lista1=[]
lista2=[]
lista3=[]
vueltas=0
while vueltas < 5:
    n = int(input("ingrese un numero a la lista 1:"))
    lista1.append(n)
    n1 = int(input("ingrese un numero  a la lista 2:"))
    lista2.append(n1)
    vueltas+=1

print(lista1)
print(lista2)

a1=0
b1=0
repeat = 0
while repeat < 5:
    suma = lista1[a1] + lista2[b1]
    lista3.append(suma)
    a1+=1
    b1+=1
    repeat += 1

print(lista3)