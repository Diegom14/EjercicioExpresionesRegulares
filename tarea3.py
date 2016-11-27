from urllib.request import urlopen # descargar una url
import re # expresiones regulares
import sys
#Fecha de fundación	o inicio	
#País de origen	
#Los álbumes publicados	en los últimos 10 años	
#Los últimos 10	singles		
#Un	link al Youtube	del	artista

#Nombre de la banda como parámetro
	
banda = sys.argv
nombre = banda[1]
if len(banda)>2:
	for i in range(2,len(banda)):
		nombre = nombre+"+"+banda[i]


url = "http://musicbrainz.org/search?query="+nombre+"&type=artist&method=indexed"

response = urlopen(url)

html = response.read()
html = html.decode('utf-8')

#lleva al link con mayor score
link = re.findall(r'<a href="/artist/([^<]+)" title=',html)
url = "http://musicbrainz.org/artist/"+link[0]
response = urlopen(url)
html = response.read()
html = html.decode('utf-8')

#busca el la fecha de inicio, pais de origen y youtube de la banda o solista
tipo = re.findall(r'<dd class="type">([^<]+)</dd>', html)

if tipo[0] =="Group":
	fundacion = re.findall(r'<dt>Founded:</dt>\n<dd>([^<]+)', html)
elif tipo[0] == "Person":
	fundacion = re.findall(r'<dt>Born:</dt>\n<dd>([^<]+)', html)

youtube = re.findall(r'<a href="//www.youtube([^<]+)">[^<]+</a>', html)

paisOrigen = re.findall(r'<dd class="area"><span class="+[^<]+"><a href="+[^<]+"><bdi>([^<]+)</bdi></a></span></dd>', html)
    
#imprime la información
for i in range(len(youtube)):
  	print("Link", i+1,":" ,"www.youtube"+youtube[i])

print("Fecha de fundación: ",fundacion[0])

print("Pais de origen :",paisOrigen[0])