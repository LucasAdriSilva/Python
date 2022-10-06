import requests, pytube
try:
    def PesquisarYoutube(Pesquisar):
        html = requests.get(f'https://www.youtube.com/results?search_query={Pesquisar}').text
        with open('text.txt', 'w+', encoding='UTF-8') as f:
            f.write(str(html))
        Teste = html.split('{"videoRenderer":{"videoId":"')[1].split('",')[0]
        return f'https://www.youtube.com/watch?v={Teste}'

    Musica = str(input('Qual o nome da música que quer baixar: '))

    pytube.YouTube(PesquisarYoutube(Musica)).streams.filter(file_extension='mp4', resolution='720p').first().download()
except Exception as e:
    print(e)