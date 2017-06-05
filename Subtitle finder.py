import re, urllib, sqlite3
from bs4 import BeautifulSoup
	

url = 'https://www.tusubtitulo.com/series.php'
url2 = 'https://www.tusubtitulo.com'
h = 'https://www.tusubtitulo.com/ajax_loadShow.php?'

listado_serie = {}
html = urllib.urlopen(url)
print "Getting Data"
soup = BeautifulSoup(html,'html.parser')
for i in soup.find_all('a'):
	link = i.get('href')
	if link.startswith('/show/'):
		nombre_serie = i.get_text()
		listado_serie[nombre_serie] = link 
		
		
print listado_serie
#Consulta

serie = raw_input("Introduzca el nombre de la serie: ")
if listado_serie.has_key(serie) == True:
	print "Encontrado " + serie
	tv_show = url2 + listado_serie[serie]
	print tv_show
else:
	print "No Encontrado, Reintente"
