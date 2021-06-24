#1. La excepción hace a la regla 
#Al menos hay dos tipos diferentes de errores en Python: 
#1.  errores de sintaxis
#2.  excepciones 

#Con cada tipo de error la máquina nos indica qué es lo que puede estar fallando de nuestro código. 

#DE SINTAXIS / DE INTERPRETACION:
# Errores en el código:  se detiene la ejecución del programa que hemos creado. 
# print(Hola mundo')
# SyntaxError: invalid syntax
#En nuestro ejemplo, el error fué detectado al ejecutar la función print(),
#ya que faltan las comillas que abre el string.


#print(3/0)
#line 16, in <module>
#   print(3/0)
#ZeroDivisionError: division by zero --> no se puede dividir con cero.


#print(divisor)
#NameError: name 'divisor' is not defined

#¿Qué nos dice el mensaje de excepción? ¿Qué es la excepción de nombre?
#nos dice que no hay ninguna variable llamada divisor. NO esta definido, no sabe que imprimir.
#NameError: no se encuentra un nombre local o global
#TypeError: Se genera cuando una operación o función se aplica a un objeto de tipo inapropiado. 


#try:
    # aquí ponemos el código que puede lanzar excepciones
#except:
    # entrará aquí en caso que se haya producido una excepción

# ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
#def division(numero, divisor):
    #try:
        #return (numero / divisor)
    #except: #except calcula todos los tipos de errores
        #print("oops hoy estoy quemada")

def division(numero, divisor):
    try:
        return (numero / divisor)
    except ZeroDivisionError:
        return ("No se puede dividir por 0")
print(division(4,2))
print(division(2,0))
#2.0
#No se puede dividir por 0


#En algunos casos, puede ser necesario crear excepciones personalizadas o forzar que ocurra una excepción específica dado un contexto. 
#La sentencia raise, se puede indicar el tipo de excepción que deseamos lanzar y el mensaje de que queremos brindarle al usuario:
#def check_int_type(x):
  #if type(x)  != int:
    #raise TypeError("Only integers are allowed")

