import requests
import json
import pprint
from bs4 import BeautifulSoup
from chaves import (CLIENT_ACCESS_TOKEN)

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


req = request_song_info('The Thrill Is Gone', 'B.B. King')

dados_musica = json.loads(req.text)
# pprint.pprint(dados_musica['response']['hits'][0]['result']['url'])
url_musica = dados_musica['response']['hits'][0]['result']['url']

letra_musica = scrap_song_url(url_musica)
print(letra_musica)
