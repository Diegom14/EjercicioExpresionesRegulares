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


if len(youtube)>0:
	for i in range(len(youtube)):
  		print("Link", i+1,":" ,"www.youtube"+youtube[i])
else:
	print("No hay informacion")
if len(fundacion)>0:
	print("Fecha de fundación: ",fundacion[0])
else:
	print("No hay informacion")

if len(paisOrigen)>0:
	print("Pais de origen :",paisOrigen[0])
else:
	print("No hay informacion")

#si el grupo tiene muchos lanzamientos estaran indexados por paginas.
pages = re.findall(r"http://musicbrainz.org/artist/"+link[0]+r"[?]+page=([0-9]{1})",html)
pages.sort()
NPages=pages[len(pages)-1]
#Esto es lento para bandas que tienen muchos lanzamientos, debido a que es necesario buscar en todos los lanzamientos
#Para los albumes de estudio no, pero para los singles si ya que no se sabe en que pagina estan
#Por lo tanto lo mas sensato es hacer una busqueda por todos los lanzamientos y hacer las dos tareas al mismo tiempo.
Albums=[]
Singles=[]
for i in range(1,int(NPages)-1):
    #print("pagina ",i)
    urlReleases="http://musicbrainz.org/artist/"+link[0]+"?page="+str(i)
    response2 = urlopen(urlReleases)
    html2 = response2.read()
    html2 = html2.decode('utf-8')

    #en cada una de las indexaciones se buscara los lanzamientos
    album=re.findall(r'<td><a href="/release-group/([^<]+)"><bdi>([^<]+)',html2)
    album_year=re.findall(r'<td class="c">([0-9]{4})',html2)
	#ahora es necesario ingresar a los links de los albumes y verificar su informacion
    for j in range(len(album)-1):
        
        url1="https://musicbrainz.org/release-group/"+album[j][0]
        response1 = urlopen(url1)
        html1= response1.read()
        html1 = html1.decode('utf-8')

        tipo=re.findall(r'<dd class="type">([^<]+)',html1)
        if tipo[0]=='Album':
            print(tipo)







