#Ej 6: 
# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y 
# multiplicar. Este objeto debe entender los siguientes mensajes:
# cargar(numero)
# sumar(numero)
# restar(numero)
# multiplicar(numero)
# valorActual()

class Calculadora:
    def __init__(self, numero = 0):
        self.numero = numero
    
    def cargar(self, numero1):
        self.numero + sel numero1
    
    def sumar(self, numero2):
        self.numero += numero2

    def restar(self, numero3):
        self.numero -= numero3
    
    def multiplicar(self, numero4):
        self.numero *= numero4
     
    def valorActual(self):
        print(self.numero)
        
calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()

#el resultado debe ser 24.