import requests
from bs4 import BeautifulSoup
from chaves import (CLIENT_ACCESS_TOKEN)

'''
Fonte
https://github.com/willamesoares/lyrics-crawler
https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62

Necessário criar uma conta no Genius para obtenção das chaves de acesso,
depois um arquivo na mesma pasta do projetos chamado chaves.py.
Dentro do arquivo terá a informação:

CLIENT_ACCESS_TOKEN = ''

Informe seu token de acesso dentro das apas.
'''

# informaçãoes padrões que serão usadas no código
defaults = {
    'request': {
        # token de acesso à API do Genius
        'token': CLIENT_ACCESS_TOKEN,
        'base_url': 'https://api.genius.com'
    }}


def request_song_info(song_title, artist_name):
    '''
    Essa função conecta via API ao site Genius e captura os dados referentes
    à uma música com o seu cantor.
    :param song_title: string, nome da musica à ser consultada
    :param artist_name: string, nome do artista à ser consultado
    :return: dicinário, contendo todos os dados da pesquisa
    '''
    base_url = defaults['request']['base_url']
    headers = {'Authorization': 'Bearer ' + defaults['request']['token']}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


def scrap_song_url(url):
    '''
    Essa função de posse da url capturada com a função request_song_info()
    faz um scraping da página e retorna a letra completa de uma música.
    :param url: string, url da música à ser consultada
    :return: string, letra completa
    '''
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics
