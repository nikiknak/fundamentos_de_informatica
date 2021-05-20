#El dominio al que estamos consultado es ponyweb.ml
import requests
r1 = requests.get("https://ponyweb.ml/v1/character/all")
print(r1.status_code)
#b) devuelve status code de 200, que quiere decir que se hizo correctamente el pedido
print(r1.headers)
#{'Date': 'Thu, 13 May 2021 13:16:47 GMT', 'Server': 'Apache/2.4.38 (Debian)', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=63072000', 'Upgrade': 
#'h2', 'Connection': 'Upgrade, Keep-Alive', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Content-Length': 
#'5670', 'Keep-Alive': 'timeout=5, max=100', 'Content-Type': 'application/json; charset=UTF-8'}
# devuelve 'Content-Type': 'application/json; Es un json

print(r1.headers['Content-Type']) 
#devuelve: application/json; charset=UTF-8

ponies = requests.get("https://ponyweb.ml/v1/character/pony")
print(ponies.json())
print(len(ponies.json())) #cantidad de ponies:2 

pony37 = requests.get("https://ponyweb.ml/v1/character/37")
print(pony37.json()) #pony 37
#devuelve:
#{'status': 200, 'data': [{'id': 37, 'name': 'Limestone Pie', 'url': 'https://mlp.fandom.com/wiki/Limestone_Pie_and_Marble_Pie', 'sex': 'Female', 'residence': 'Pie Family 
#Rock Farm, Rockville, Western Equestria', 'kind': ['Earth'], 'image': ['https://vignette.wikia.nocookie.net/mlp/images/a/a2/Limestone_Pie_ID_S5E20.png/revision/latest?cb=20151024190324', 'https://vignette.wikia.nocookie.net/mlp/images/9/96/Limestone_Pie_id_S1E23.png/revision/latest?cb=20110825215431']}]}

song = requests.get("https://ponyweb.ml/v1/character/song/all")
print(song.json())

path = "/Users/niki/Desktop/INFORMATICA/archivo_nuevos.txt"
with open(path, 'w') as file:
    file.write("{'status': 200, 'data': [{'id': 37, 'name': 'Limestone Pie', 'url': 'https://mlp.fandom.com/wiki/Limestone_Pie_and_Marble_Pie', 'sex': 'Female', 'residence': 'Pie Family Rock Farm, Rockville, Western Equestria', 'kind': ['Earth'], 'image': ['https://vignette.wikia.nocookie.net/mlp/images/a/a2/Limestone_Pie_ID_S5E20.png/revision/latest?cb=20151024190324', 'https://vignette.wikia.nocookie.net/mlp/images/9/96/Limestone_Pie_id_S1E23.png/revision/latest?cb=20110825215431']}]}")
    