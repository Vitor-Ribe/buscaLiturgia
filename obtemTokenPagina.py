# Caso você não consiga um token de acesso a página, pode usar este código para gerar um através de seu token de usuário. Todas os pré-requisitos listados no READ-ME devem ser cumpridos para que esse código funcione.
import requests

user_access_token = 'SEU_TOKEN_DE_USUARIO'  # Substitua pelo seu token de usuário
page_id = 'ID_DA_PAGINA'  # Substitua pelo ID da página que deseja o token

# URL para obter o token da página
url = f'https://graph.facebook.com/{page_id}?fields=access_token&access_token={user_access_token}'

response = requests.get(url)
page_access_token = response.json().get('access_token')

print(f'Token de acesso da página: {page_access_token}')
