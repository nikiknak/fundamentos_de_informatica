#Ejercicio 2
#Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

class Golondrina:
    def __init__(self,energia):
        self.energia = energia
    def comer_alpiste(self,gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)
    
    def volar(self,kms):
        self.energia -= 10 +kms

    def esta_debil(self):
        return self.energia < 10

    def saciar(self):
        self.comer_apliste(75)

    def esta_equilibrio(self):
        print(self.energia > 150 and self.energia < 300)
    
    pepito = Golondrina(200)
    pepito.esta_equilibrio()