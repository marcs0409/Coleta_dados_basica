#https://br.investing.com/indices/bovespa-historical-data

import pandas
import io
import requests
from bs4 import BeautifulSoup

# Define a User-Agent to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print('Requests: ')
url = 'https://br.investing.com/indices/bovespa-historical-data'
response = requests.get(url, headers=headers)
print(response.text[:600])

print('\nBeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('\nPandas: ')
# Pass the HTML text directly to read_html instead of the URL to avoid 403 Forbidden
url_dados = pandas.read_html(io.StringIO(response.text))
print(url_dados[0].head(10))