#Ejercicio 2
#Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

class Ave: 
    def esta_feliz(self):
        return self.energia > 500

    def arranca_en(self, ciudad):
        self.ciudad_actual = ciudad

    def volar_por_panamericana(self, ciudad_destino):
        kms = abs(self.ciudad_actual - ciudad_destino)
        self.volar(kms)
        self.ciudad_actual = ciudad_destino

class Golondrina(Ave): 
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia = self.energia + 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_debil(self):
        return self.energia <= 10

    def saciar(self):
        self.comer_alpiste(100)
    
    def esta_en_equilibrio(self):
        return self.energia > 150 and self.energia < 300 

pepita = Golondrina(100) 
print(pepita.esta_en_equilibrio()) 
pepita.comer_alpiste(15) 
print(pepita.energia) 
print(pepita.esta_en_equilibrio()) 
