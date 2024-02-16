import requests # É uma biblioteca Python para fazer requisições HTTP.
from bs4 import BeautifulSoup # É uma biblioteca de software de código aberto para Python usada para extrair dados de documentos HTML e XML.

# Definindo a URL do site - Pagina do G.E. de notícias de time de futebol
url = "https://ge.globo.com/pa/futebol/times/paysandu/"

# Fazendo a requisição GET
requisicao = requests.get(url)

# Verificando o status da requisição
if requisicao.status_code == 200:

    # Extraindo o conteúdo HTML da página
    pagina = BeautifulSoup(requisicao.text, "html.parser")

    # Localizando todas as notícias
    noticias = pagina.find_all("a", class_="feed-post-link")

    # Iterando sobre as notícias
    for i, noticia in enumerate(noticias, start=1):

        # Extraindo o título da notícia
        titulo = noticia.text

        # Extraindo o link da notícia
        link = noticia.get("href")

        # Extraindo a data e hora da notícia 
        data_hora = noticia.find("span", class_="feed-post-datatime")  # Não está retornando nenhum dado
        
        # Verificando se a data e hora foram encontradas
        if data_hora:
            data_hora = data_hora.text
        else:
            data_hora = "Data não disponível para este site"

        # Imprimindo as informações da notícia
        print(f'Notícia {i}: {titulo}')
        print(f'Link: {link}')
        print(f'Foi postado há: {data_hora}') #No momento, não está funcionando.
        print('')

else:
    print(f'Erro ao acessar a URL: {url}')
    print(f'Código de status: {requisicao.status_code}')    
