# buscaLiturgia
Programa para buscar liturgia em sites e postar no feed de uma página católica.

O programa usa o site [Liturgia Diária](https://liturgia.cancaonova.com/pb/) como fonte dos evangelhos.

Ele salva o texto em um arquivo .txt, para caso queira utilizá-lo posteriormente, como compartilhá-lo em outras Redes Sociais,
Por fim ele sobe esse texto em um post na página a qual foi atribuída o ID no programa. 

Para o programa funcionar, você precisa ter um Token de página disponibilizado pelo Facebook através do site [developers.facebook.com](https://developers.facebook.com/), assim como o ID da página que vc quer postar. PS: Seu perfil pessoal precisa ter acesso como administrador a essa página para conseguir postar através da API.

O programa usa as bibliotecas BeaultifulSoup e Requests para extrair o evangelho do site, e usa um Token de Página da GRAPH API do Facebook para postagem.
