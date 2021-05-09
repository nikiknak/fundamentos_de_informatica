#2: Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda
#  volar si al hacerlo la energía toma el valor 0 o valor negativo.
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (10 + kms > self.energia): # si la que energia q va a gastar es menor a la tiene 
        self.energia -= 10 + kms # que vuele
    else:
        print("No puedo volar esa distancia, no tengo suficiente energia, necesito comer alpiste")
  def esta_debil(self):
    return self.energia <= 10
  def esta_feliz(self):
    return self.energia >= 200
  
  pepita = Golondrina(100)
  pepita.volar(9)
  print(pepita.energia)
  pepita.volar(100)