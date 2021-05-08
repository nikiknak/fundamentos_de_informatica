"""#Compra de una casa
Determinar cuánto tiempo, (meses), tomaría ahorrar la cantidad suficiente de dinero para pagar el depósito.
Consideremos que se realiza una inversión con el dinero ahorrado con una ganacia del 4% anual.

Datos y variables

costo_total, porcentaje_deposito (25% costo total), cantidad_ahorrada(inicia en 0), sueldo_anual, g(ganacia 4% anual),
porcentaje_ahorrado(% del sueldo), sueldo_mensual
"""

costo_total = int(input("Ingrese el costo total de la propiedad:"))

sueldo_anual = int(input("Ingrese su sueldo anual:"))

porcentaje_ahorrado = float(input("Ingrese la proporcion de sueldo que quiere ahorrar mensualmente:"))

deposito = costo_total * 0.25
cantidad_ahorrada = 0
tasa_interes = 0.04
tasa_mensual = tasa_interes/12
sueldo_mensual= sueldo_anual/12
ahorro_mensual = sueldo_mensual * porcentaje_ahorrado

print(deposito)
print(sueldo_mensual)
print(ahorro_mensual)

r = tasa_mensual
mes = 0
ahorros = 0
while ahorros <= deposito:
  mes += 1
  ahorros += ahorro_mensual
  ahorros = ahorros * (1 + r )

print("En " + str(mes) + " meses lograrias ahorrar la suma de: $" + str(int(ahorros)) + ", alcanzando asi el total del deposito")

ganancia = ahorros - (ahorro_mensual*mes)
print("\nObtuviste una ganancia de: $"+str(int(ganancia)))