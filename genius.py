import requests
from bs4 import BeautifulSoup
from chaves import (CLIENT_ACCESS_TOKEN)
import json

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

defaults = {
    'request': {
        'token': CLIENT_ACCESS_TOKEN,
        'base_url': 'https://api.genius.com'
    }}


def request_song_info(song_title, artist_name):
    base_url = defaults['request']['base_url']
    headers = {'Authorization': 'Bearer ' + defaults['request']['token']}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics
