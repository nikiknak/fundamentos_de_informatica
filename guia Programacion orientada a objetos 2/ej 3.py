"""Ejercicio 3
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no."""

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer(self, gramos): #cambiamos comer_alpiste a comer
    self.energia += 4 * gramos

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

class Gorrion:
    def __init__(self, kms, gramos):
        self.kms = kms
        self.gramos = gramos
        self.comidas = []
        self.vuelos = []
    def volar(self, longitud):
        if longitud > 0:
            self.vuelos.append(longitud)
            self.kms += longitud   
    def comer(self, ingerido):
        if ingerido > 0:
            self.comidas.append(ingerido)
            self.gramos += ingerido   
    def CSS(self):
        if self.gramos <= 0:
            return 
        else:
            return self.kms / self.gramos
    def CSSP(self):
        if self.gramos <= 0:
            return 
        else:
            return int(max(self.vuelos)) / int(max(self.comidas))
    def CSSV(self):
        if len(self.comidas) <= 0:
            return 
        else:
            return int(len(self.vuelos)/len(self.comidas))
    def esta_en_equilibrio(self): #hacemos un metodo esta_en_equilibrio para el Gorrion que no tenia
        return self.gramos > 100 and self.gramos < 300 

class Ornitologo:
    def __init__(self):
        self.aves = []
    def estudiarAve(self, ave):
        self.aves.append(ave)
    def avesEnEstudio():
        return self.aves
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.comer(80)
            ave.volar(70)
            ave.comer(10)
    def avesEnEquilibrio(self,ave):
        return ave.esta_en_equilibrio()

perry = Ornitologo() 
julieta = Golondrina(200) 
print(julieta.energia)
maria = Golondrina(300) 
jorge = Gorrion(20,30) 
pedro = Gorrion(10,20) 
perry.estudiarAve(julieta)
perry.estudiarAve(jorge)
perry.estudiarAve(pedro)

print(perry.avesEnEstudio)
perry.realizarRutinaSobreAves()

print(jorge.vuelos) 
print(jorge.comidas) 
print(jorge.kms) 
print(jorge.gramos) 
print(perry.avesEnEquilibrio(jorge))  

print(pedro.vuelos) 
print(pedro.comidas) 
print(pedro.kms) 
print(pedro.gramos) 
print(perry.avesEnEquilibrio(pedro)) 

print(julieta.energia) ¡
print(perry.avesEnEquilibrio(julieta)) 
 
print(maria.energia) 