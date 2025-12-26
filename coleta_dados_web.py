import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('total de titulos: ', contar_titulos)
print('total de paragrafos: ', contar_paragrafos, '\n')

# Exibir somente o texto das tags h2 e p
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('Titulo: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)

# Exibir tags aninhadas
for titulo in extracao.find_all('h2'):
    print('Titulo: \n', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), '| URL: ', a['href'])