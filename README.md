# 🎬 TMDB CLI App

Uma ferramenta de linha de comando (CLI) simples e eficiente desenvolvida em Python para explorar os filmes do The Movie Database (TMDB) direto do terminal.

---

## 🚀 Funcionalidades

* Consulta em tempo real das seguintes listas de filmes:
  * `playing`: Filmes que estão em cartaz.
  * `popular`: Filmes populares do momento.
  * `top`: Filmes mais bem avaliados de todos os tempos.
  * `upcoming`: Próximos lançamentos.
* Interface intuitiva via terminal (CLI).
* Retorno de dados formatado com título, nota e data de lançamento.

---

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* **Python 3.8** ou superior.
* Uma chave de acesso (Bearer Token) da [API do TMDB](https://www.themoviedb.org/).

---

## 📦 Instalação

   Clone este repositório:
   ```bash
   git clone [https://github.com/goesEduardo/tmdb-app.git](https://github.com/goesEduardo/tmdb-app.git)
   cd tmdb-app



🔧 Configuração
Abra o arquivo tmdb_app.py e insira o seu token de autenticação na linha indicada:

Python
headers = {
    "accept": "application/json",
    "Authorization": "Bearer SEU_BEARER_TOKEN_AQUI"
}

💻 Como Usar
Para rodar o aplicativo, use o argumento --type (ou -t) seguido de uma das opções válidas:

Bash
# Para ver os filmes mais populares
tmdb-app --type "popular"

# Para ver os filmes que estão em cartaz
tmdb-app --type "playing"

## 🔗 Links Úteis

* 💻 [Repositório do Projeto] <https://github.com/GoesEduardo/tmdb-app>
* 📖 [Documentação da API do TMDB] <https://developer.themoviedb.org/docs>
* 🐛 [Reportar Problemas / Bugs] <https://github.com/GoesEduardo/tmdb-app/issues>

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
