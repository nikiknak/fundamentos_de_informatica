#14: Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
import re 
texto = "Lista de Supermercado:\nPapa-Batata_Calabaza,Queso, Tomate\t."
patron = "[\s]"
print(texto)
print(re.sub(patron, ";", texto))