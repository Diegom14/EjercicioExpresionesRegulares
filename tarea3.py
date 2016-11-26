from urllib.request import urlopen # descargar una url
import re # expresiones regulares

#Fecha de fundación	o inicio	
#País de origen	
#Los álbumes publicados	en los últimos 10 años	
#Los últimos 10	singles		
#Un	link al Youtube	del	artista



if __name__ == "__main__":
    # descargar una url
    url = 'http://musicbrainz.org/artist/e99f6d62-f62b-4e1e-8593-33d5696d85f0'
    response = urlopen(url)
    html = response.read()
    html = html.decode('utf-8')

    youtube = re.findall(r'<a href="//www.youtube([^<]+)">[^<]+</a>', html)
    fundacion = re.findall(r'<dt>Founded:</dt>\n<dd>([^<]+)', html)

    paisOrigen = re.findall(r'<dd class="area"><span class="+[^<]+"><a href="+[^<]+"><bdi>([^<]+)</bdi></a></span></dd>', html)
    
    for i in range(len(youtube)):
    	print("Link", i+1,":" ,"www.youtube"+youtube[i])

    print("Fecha de fundación: ",fundacion)

    print(paisOrigen)
    