from genius import *
import json
import time

cantor = 'Gary Clark Jr.'

'''
Lista de musicas capturada de forma manual, proximo passo descobrir uma forma de
capturar todas aos nomes das musicas de uma cantor/compositor.
'''

# abre o arquivo que contém a lista dos nomes das músicas
arq = open('lista_musicas/gary_clarck_jr_music_list.txt', 'r')

# salva a as musicas na varíavel lista_musica
lista_musica = arq.readlines()

'''
Esse for entra na lista de musicas e captura as musicas via API do genius e salva cada uma
em um arquivo separado, tendo o nome do arquivo montado como autor + titulo
'''
for musica in lista_musica:
    # começa o laço e captura cada música uma a uma
    # a variavel req recebe da API os dados completos sobre a música
    req = request_song_info(musica, cantor)
    # dados_musica recebe o req convertido em dicionário
    dados_musica = json.loads(req.text)
    # titulo da musica vindo da API
    titulo = dados_musica['response']['hits'][0]['result']['title']
    # autor da musica vindo da API
    autor = dados_musica['response']['hits'][0]['result']['primary_artist']['name']
    # url_musica recebe a url da musica no site do Genius para porde fazer o scrap
    url_musica = dados_musica['response']['hits'][0]['result']['url']
    # letra_musica recebe apenas a letra da musica
    letra_musica = scrap_song_url(url_musica)
    # Confirmação na tela de que a música foi salva, criar aqui uma verificação melhor (try, except)
    print('Musica', titulo, 'salva!')
    # monta o nome do arquivo para ser salvo
    nome_arquivo = autor + ' - ' + titulo
    # cria o arquivo que será salvo contendo cada letra de musica separadamente
    arquivo = open('letras/' + str(nome_arquivo) + '.txt', 'w')
    # salva a letra no .txt
    arquivo.writelines(letra_musica)
    # fecha o arquivo
    arquivo.close()
    # intervalo de 2 segundo entre uma chamada e outra da API, não sei se tem um limite ou não
    time.sleep(2)

# Fecha o arquivo que contém os nomes das músicas
arq.close()
