from genius import *
import json
# para visualizar mais amigavelmente o dicionario que vem do site
import pprint
import time

cantor = 'Gary Clark Jr.'

# lista de musicas capturar à mão, proximo passo descobrir uma forma de
# capturar todas aos nomes das musicas de uma cantor/compositor x
arq = open('lista_musicas/gary_clarck_jr_music_list.txt', 'r')
lista_musica = arq.readlines()

for musica in lista_musica:
    req = request_song_info(musica, cantor)
    dados_musica = json.loads(req.text)
    titulo = dados_musica['response']['hits'][0]['result']['title']
    autor = dados_musica['response']['hits'][0]['result']['primary_artist']['name']
    #  print(autor + ' - ' + titulo)
    url_musica = dados_musica['response']['hits'][0]['result']['url']
    letra_musica = scrap_song_url(url_musica)
    #  print(letra_musica)
    print('Musica', titulo, 'salva!')
    nome_arquivo = autor + ' - ' + titulo
    arquivo = open('letras/' + str(nome_arquivo) + '.txt', 'w')
    arquivo.writelines(letra_musica)
    arquivo.close()

    time.sleep(2)

arq.close()
