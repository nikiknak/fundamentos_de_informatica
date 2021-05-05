# Ej5: 
# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último 
# comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: 
# "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo).
# El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la 
# serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
    def __init__(self, valor):
        self.valor = valor  
        self.comando = ""
        
    def inc(self):
        self.valor += 1
        self.comando = 'incremento'

    def dis(self):
        self.valor -= 1
        self.comando = 'disminucion'
    
    def reset(self):
        self.valor == 0
        self.comando = 'reset'
     
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

    def valorActual(self):
        print(self.valor)

    def ultimoComando(self):
        print(self.comando)



contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
contador.ultimoComando()
    
