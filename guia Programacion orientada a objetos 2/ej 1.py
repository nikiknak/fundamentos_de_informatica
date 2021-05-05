#Ejercicio 1
#Dadas las siguientes clases responder:

#cuales son sus estados

#cuales son sus interfaces

#¿Comparten interfaz?

#¿Son polimórficas? 

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4

    #Estado: es el conjunto de atributos
    #Estado de Perro: alimento y caricias
    #Estado de Gato: alimento y caricias
    # interfaz es el conjunto de metodos
    #interfaz de Perro: energia,comer,alimento,acariciar,estaDebil y pasear
    #interfaz de Gato: energia,comer, caricias, acariciar y estaDebil

    #comparten parte de la interfaz
    # No son polimorficas porque no hay una extra clase que las use indistintamente.
    