import re, urllib, sqlite3
from bs4 import BeautifulSoup
	

url = 'https://www.tusubtitulo.com/series.php'
url2 = 'https://www.tusubtitulo.com'
h = 'https://www.tusubtitulo.com/ajax_loadShow.php?'

serie = list()
html = urllib.urlopen(url)
soup = BeautifulSoup(html,'html.parser')
for i in soup('a'):
	link = i.get('href')
	if link.startswith('/show/'):
		serie.append(link)
		nombre_serie = i.get_text()
		print nombre_serie
		
for j in serie:
	tvshow = re.findall('[0-9]+', j)
	for index in tvshow:
		serie.append(index)

cont = 0
num_season = 1
while x < len(serie):
	tv_show = serie[cont]
	cont = cont + 1
	campos = urllib.urlencode({'show': tv_show , 'season': season})
	url3 = urllib.urlopen(h , campos)
	num_season = num_season + 1
	soup = BeautifulSoup(url3 , 'html.parser')
	print soup
	for i in soup('a'):
		print i
