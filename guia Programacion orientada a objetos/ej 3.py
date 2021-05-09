#3: Creá una clase Notebook cuyo estado sea: marca, modelo y precio, 
# y que tenga un método que le aplique un descuento al precio, el cual tiene
# que recibir un número entero (el porcentaje de descuento) y tiene que devolver 
# cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar 
# esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __int__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento (self, numero):
        descuento = (numero/100)* self.precio
        return(self.precio - descuento)

mac = Notebook("apple", "air", 1000)
print(mac.descuento(34))