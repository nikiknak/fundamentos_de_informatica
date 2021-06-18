import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
print(r.json())
#{'id': 1, 'tipo': 'pantalon', 'talle': 35}
#json --> me trae la informacion de ese servidor, me la devuelve en forma de diccionario, estructura de llave.
#servidor --> guarda la informacion de la ropa

# DESAFIO I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
#{
#  "id": 20,
#  "tipo": "saco",
#  "talle": "XL"
#}
r2 = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(r2.json())
#{'id': 20, 'tipo': 'saco', 'talle': 'XL'}

#2. CODIGOS DE RESPUESTA
# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
r3 = requests.get('https://macowins-server.herokuapp.com/prendas/400')
#print(r3.json())
#salta un error
print(r3.status_code) #404: es un error, no encuentra el recurso que estaba buscando

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
# Para pensar: ¿Qué cambió? ¿Qué cambio o cambios te parecen relevates entre ambas respuestas? ¿Qué emoji le pondrías a esta respuesta?
print(r.headers) #los headers nos tira la información que pedimos, que tipo de datos hay. Toda la metadata que esta asociada a lo que se pide. 
#{'Server': 'Cowboy', 
#'Connection': 'keep-alive', 
#'X-Powered-By': 'Express', 
#'Expires': '-1', 
#'Content-Type': 'application/json; charset=utf-8', 
#'Content-Length': '50', 
#'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 
#'Vary': 'Accept-Encoding', 'Date': 'Sat, 27 Feb 2021 18:11:12 GMT',
#'Via': '1.1 vegur'}
print(r.status_code) #200, esta bien, esta en el servidor.  

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
r4 = requests.get('https://macowins-server.herokuapp.com/prindas/1')
print(r4.status_code) #404, error.

r5 = requests.get("https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien")
print(r5.status_code) #500. Un mensaje de error genérico, condición inesperada.
print(r5.headers)
#{'Server': 'Cowboy', 
#'Connection': 'keep-alive',
# 'X-Powered-By': 'Express', 
# 'Vary': 'Origin, Accept-Encoding', 
# 'Access-Control-Allow-Credentials': 'true', 
# 'Cache-Control': 'no-cache', 
# 'Pragma': 'no-cache', 
# 'Expires': '-1', 
# 'Content-Security-Policy': "default-src 'none'", 
# 'X-Content-Type-Options': 'nosniff',
# 'Content-Type': 'text/html; charset=utf-8', 
# 'Content-Length': '148', 
# 'Date': 'Mon, 01 Mar 2021 20:18:38 GMT', 
# 'Via': '1.1 vegur'}
print(r5.content)
#b'<!DOCTYPE html>
#  <html lang="en">
#      <head>
#      <meta charset="utf-8">
#        <title>Error</title>
#      </head>
#      <body>
#        <pre>Internal Server Error</pre>
#      </body>
#  </html>'
#Autoevaluación: ¿qué representa el código 500? 
#un error en el servidor = 500

#3. PARAMETROS
# Hagamos un nuevo pedido, pero ahora a una ruta ligeramente diferente:
# Para pensar: ¿es lo mismo consultar /prendas/ que /prendas/1? ¿En qué se diferencian? ¿Qué ocurre si hacemos r.content? ¿Por qué?
r5 = requests.get("https://macowins-server.herokuapp.com/prendas") # me devuelve todas las prendas que se encuentran en forma de diccionario
print(type(r5.json())) 
print(r5.status_code) # me devuelve : 200, esta bien, lo encontro. 

print(r.content)
#b'[\n  {\n    "id": 1,\n    "tipo": "pantalon",\n    "talle": 35\n  },\n  {\n    "id": 2,\n    "tipo": "pantalon",\n    "talle": 36\n  },\n  {\n    "id": 3,\n    "tipo": "pantalon",\n    "talle": 37\n  },\n  {\n    "id": 4,\n    "tipo": "pantalon",\n    "talle": 38\n  },\n  {\n    "id": 5,\n    "tipo": "pantalon",\n    "talle": 39\n  },\n  {\n   
# "id": 6,\n    "tipo": "pantalon",\n    "talle": 40\n  },\n  {\n    "id": 7,\n    "tipo": "pantalon",\n    "talle": 
#41\n  },\n  {\n    "id": 8,\n    "tipo": "pantalon",\n    
#"talle": 42\n  },\n  {\n    "id": 9,\n    "tipo": "pantalon",\n    "talle": 43\n  },\n  {\n    "id": 10,\n    "tipo": "pantalon",\n    "talle": 44\n  },\n  {\n    "id": 11,\n    "tipo": "remera",\n    "talle": "XS"\n  },\n  {\n    "id": 12,\n    "tipo": "remera",\n    "talle": "S"\n  },\n 
# {\n    "id": 13,\n    "tipo": "remera",\n    "talle": "M"\n  },\n  {\n    "id": 14,\n    "tipo": "remera",\n    "talle": "L"\n  },\n  {\n    "id": 15,\n    "tipo": "remera",\n    "talle": "XL"\n  },\n  {\n    "id": 16,\n    "tipo": "saco",\n    "talle": "XS"\n  },\n  {\n    "id": 17,\n   
# "tipo": "saco",\n    "talle": "S"\n  },\n  {\n    "id": 18,\n    "tipo": "saco",\n    "talle": "M",\n    "enStock": false\n  },\n  {\n    "id": 19,\n    "tipo": "saco",\n   
# "talle": "L"\n  },\n  {\n    "id": 20,\n    "tipo": "saco",\n    "talle": "XL"\n  }\n]'

#r = requests.get("https://macowins-server.herokuapp.com/prendas/1") 
#print(r.json()) # le pedimos el primer diccionanrio de la lista, es decir con id = 1.

# DESAFIO V: 
# Para pensar: ¿qué hará /ventas/2? ¿/ventas/?.
r6 = requests.get("https://macowins-server.herokuapp.com/ventas") # me devuelve todas las ventas
print(r6.json()) 

r7 = requests.get("https://macowins-server.herokuapp.com/ventas/2")# me devuelve la venta con id = 2
print(r7.json())

r8 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon")
print(r8.json())
# Autoevaluación: ¿qué acabamos de hacer? ¿para qué nos sirvió el ?...=...?
# Me tira todos los pantalones que hay y sus descripciones
r9 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=saco")
print(r9.json())
# me devuelve todos las prendas de tipo saco.

# Desafío VI: Obtené las remeras.
r10 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera")
print(r10.json())

talle40= requests.get('https://macowins-server.herokuapp.com/prendas?talle=40')
print(talle40.json()) # solo hay una prenda talle 40 y es de tipo pantalon.

r11 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon")
print(r11.json()) 


# Desafío VII: Obtené las remeras XS
r12 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=XS&tipo=remera")
print(r12.json())

# Desafío VIII:
#Por ejemplo cerebro://recuerdos:3403/recientes#hoy?tema=http es sólo un string que cumple la estructura de una URI, aunque probablemente no sea muy util (o al menos no el año 2020 🧠)
#decí usando tus palabras qué significa la URI de este ejemplo cerebral.
# los recuerdos que se obtubieron del dia de hoy 
# timeout:sirve para que en un determinado tiempo (lapso de de segundos) siga buscando si es que no se encontro nada.

#Para pensar: ¿por qué Google tiene múltiples IPs? ¿Que ventaja representa para esta empresa y para quienes lo usamos?
#reducen el tráfico en la red.
# ventajas: que reduce la sobrecarga de la página y potenciales errores que puedan llegar a aparecer.

#Desafío IX: ¿a través de qué IP accedés a google desde tu computadora? # desde la interfaz de la red del wifi.

# 6.Cabeceras
# Para pensar: ¿Cuál fue el Content-Type de las respuesta del ejemplo? ¿Por qué devolvió eso?
#Content-Type: application/json; charset=utf-8  es el tipo de contenido que estamos recibiendo y estamos utilizando json.

#Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio? Averiguá el Content-Type de /home
u = requests.get('https://macowins-server.herokuapp.com/home')
print(u.headers)
#Content-Type': 'text/html; charset=utf-8'
#¿Para qué sirven las cabeceras? Mencioná al menos dos.
#las cabeceras devuelven informacion relevante: content-type nos dice el tipo de contenido de la URL y content-lenght nos devuelve el tamaño de la respuesta.
# Tambien se encuentran: X-Powered-By y Date.

# 7. Desde el navegador
#Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se transfiere encriptado, y la fecha de expieración del contenido.

#1.  ucema:
ucema = requests.get('https://ucema.edu.ar/comunidad')
print(ucema.headers)
#Server': 'nginx
#Expires': 'Sun, 19 Nov 1978 05:00:00 GMT"
#Accept-Encoding, Cookie'
#2. mail:
mail = requests.get("https://mail.google.com/mail/u/0/#sent")
print(mail.headers)
#3. doc google:
google = requests.get("https://docs.google.com/document/u/0/")
print(google.headers)
#Accept-Encoding'
#Expires': 'Fri, 01 Jan 1990 00:00:00 GMT'
#4. netflix:
net=("https://www.netflix.com/browse")
print(net.headers)
#'Server': 'GitHub.com'
#Expires=Sat, 18 Jun 2022 00:46:30 GMT
#Accept-Encoding

# 8. Borrando contenido
# Para pensar: ¿es correcto que permitamos que cualquiera borre contenido?
# No, solo los los administradores encragados del area tendrian que tener acceso.

#Para pensar: Estuvimos usando un método específico de request GET, que servía para... 
# ¿Para qué servía? ¿Qué crees que hará DELETE?
#get nos devuelve los datos. Delete nos borra los datos 

# Para pensar: ¿Habrá algo que impida que no borre nada con un DELETE, o que borre algo con un GET?
# la encriptación y configuración de la página estara a cargo. 

# 9. Creando y actualizando contenido:
#Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
#data = {'id': 21}
#r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
# nos devuelve el codigo 201.

#Para pensar: ¿Nos es realmente útil crear una prenda sin especificar más nada?
#no, se tendria que especificar que tipo de prendas se encuentran, talles, colores, material, etc.
#Para pensar: ¿Por qué se creó con el id 21?
# porque estoy ingresando un nuevo item y continua en la serie.

#data =  { "tipo": "chomba", "talle": "XS" }
#r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)

#Autoevaluación: ¿para qué sirve el parámetro data? para ingresar un nuevo item.
#Para pensar: Hmm, funcionó, pero ¿creó el contenido que queríamos? ¿Por qué? no lo creo porque falto ingresar el id del nuevo item.


#Desafío XIII: Creá una venta.
data = { "id": 1502, "producto": { "tipo": "pantalon", "talle": 4 }, "fecha": "2020-04-7T21:01:12.000Z" }
i = requests.post('https://macowins-server.herokuapp.com/ventas', data=data)

# Desafío XIV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede?
r13 = requests.post("https://macowins-server.herokuapp.com/prendas/1")
print(r13.status_code)#404
print(r13.json()) #tira error no se pudo.

#10. Sobre la semántica de los verbos
#Para pensar: A los métodos HTTP también se les dice verbos. ¿Por qué?
# porque hay varios metodos de HTTP como los verbos. 

#Para pensar: ¿por qué es importante respetar estas convenciones?
# para identificar que estamos haciendo y no confundirnos.

#Para pensar: POST es uno de los métodos con efecto más antiguos de HTTP,
# y por eso es común que a veces se lo use para resolver operaciones que 
# no encajan en otras semánticas. ¿Se te ocurre algún otro ejemplo fuera de HTTP 
# en que pase algo así?
#  ejemplo Banco, puede ser un banco de la plaza o el banco donde retiras plata.

#11. Recursos
#Desafío XV: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?

#•	Github : si
#•	Youtube : no 
#•	Facebook : si
#•	Infobae, Pagina12, La Nacion : si
#•	UNQ, UCEMA : si 

#Desafío XVI: si no se organizan de forma REST, ¿cómo se organizan sus rutas?
# se podrain organizar por el id del video 

