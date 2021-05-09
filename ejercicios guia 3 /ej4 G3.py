#4: Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re
string = "Buen_dia"
patron = "(\w*)_(\w*)"
print(re.findall(patron, string))
print(re.search(patron, string))