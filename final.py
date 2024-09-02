import requests
from bs4 import BeautifulSoup

link = "https://liturgia.cancaonova.com/pb/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

# requisição do link
requisicao = requests.get(link, headers=headers)

# recebe o html bagunçado do site e o organiza
site = BeautifulSoup(requisicao.text, "html.parser")

# recebe dados da linha html
evangelho = site.find("div", id="liturgia-4")
# pega a informação em formato de texto
if evangelho:
    textoEvangelho = evangelho.get_text()
    print(textoEvangelho)
    # Salvando o texto em um arquivo .txt
    with open("evangelho.txt", "w", encoding="utf-8") as file:
        file.write(textoEvangelho)
    print("\nTexto salvo com sucesso no arquivo 'evangelho.txt'.")

    # Token de acesso da página (substitua pelo seu token)
    access_token = 'SEU_TOKEN_DE_ACESSO_AQUI'

    # ID da página no Facebook (substitua pelo ID da sua página)
    page_id = 'ID_DA_PAGINA_AQUI'

    # URL da API para postar na página
    url = f'https://graph.facebook.com/{page_id}/feed'

    # Dados da postagem
    payload = {
        'message': textoEvangelho,
        'access_token': access_token
    }

    # Fazendo a requisição POST para publicar na página do Facebook
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Texto postado com sucesso na página do Facebook.")
    else:
        print(f"Erro ao postar no Facebook: {response.json()}")
else:
    print("Div com id 'liturgia-4' não encontrada.")
