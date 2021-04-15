#2: Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).
nro = float(input("Dame un número:"))
def lector_de_nro (numero):
    if numero == 0:
        print("El número",numero, "es 0 y es par")
    elif numero > 0 and numero % 2 == 0:
        print("El número",numero, "es positivo y es par")
    elif numero > 0 and numero % 2 != 0:
        print("El número",numero, "es positivo y es impar")
    elif numero < 0 and numero % 2 != 0:
        print("El número",numero, "es negativo y es impar")
    elif numero < 0 and numero % 2 == 0:
        print("El número",numero, "es negativo y es par")
lector_de_nro(nro)