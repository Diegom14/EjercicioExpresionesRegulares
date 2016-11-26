from urllib.request import urlopen # descargar una url
import re # expresiones regulares

#Fecha de fundación	o inicio	
#País de origen	
#Los álbumes publicados	en los últimos 10 años	
#Los últimos 10	singles		
#Un	link al Youtube	del	artista



if __name__ == "__main__":
    # descargar una url
    url = 'http://musicbrainz.org/artist/65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab'
    response = urlopen(url)
    html = response.read()
    html = html.decode('utf-8')

    youtube = re.findall(r' <a href="//([^<]+)">[^<]+VEVO', html)
    youtube2 = re.findall(r' <a href="//([^<]+)">[^<]+TV', html)
    
    fundacion = re.findall(r'<dt>Founded:</dt>\n<dd>([^<]+)', html)

    print("Link 1: ",youtube[0],"\n","Link 2: ",youtube2[0])

    print("Fecha de fundación: ",fundacion[0])

    