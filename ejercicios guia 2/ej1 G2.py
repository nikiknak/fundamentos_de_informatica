#1: Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
cadena = str(input("Dame una palabra:"))
def es_mayus(palabra):
    if palabra[0] >= "a" and palabra[0] <="z":
        print("Es minúscula")
    else:
        print("Es mayúscula")
es_mayus(cadena)

