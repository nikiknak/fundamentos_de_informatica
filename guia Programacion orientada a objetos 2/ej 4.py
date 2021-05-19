"""Ejercicio 4
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

comienzan con una cantidad que podemos establecer de combustible

los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera."""

class MediodeTransporte:
    def __init__(self,combustible = 100):
        self.combustible = combustible
        def cargar_combustible (self, cantidad):
            self.cargar_combustible = self.combustible + cantidad
        def combustible_actual(self):
            self.cargar_combustible = self.combustible_actual
        def cantidad_personas( self, personas):
            self.cantidad_personas = personas <= self.max_personas
            
class Auto(MediodeTransporte):
        def max_personas(self):
            self.max_personas = 5
            return self.max_personas
        def distancia (self, km):
            self.distancia = self.combustible - (1/2 * km)
        
class Moto(MediodeTransporte):
        def max_personas(self):
            self.max_personas = 2
            return self.max_personas
        def distancia (self,km):
            self.distancia = self.combustible - (1 * km)

        
moto1 = Moto(200)
moto2 = Moto()
auto1 = Auto(300)
auto2 = Auto()

print(moto1.cantidad_personas(3))
print(moto1.cantidad_personas(2))

