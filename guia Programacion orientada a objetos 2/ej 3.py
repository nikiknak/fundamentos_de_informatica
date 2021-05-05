"""Ejercicio 3
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no."""

class Ornitologo():
    def __init__(self):
        self.aves =[]
    def estudiar_ave(self, ave):
        self.aves.append(ave)
    def avesEnEstudio(self):
        print(self.aves)
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.comer(0)
            ave.volar()
            ave.comer(-70)
    def avesENEquilibrio(self):
        for ave in self.aves:
            ave.equilibrio()