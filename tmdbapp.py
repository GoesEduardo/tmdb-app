import requests
import argparse
import sys


def buscar_filme(tipoBusca):
   
    endpoints = {
        "playing": "now_playing",
        "popular": "popular",
        "top": "top_rated",
        "upcoming": "upcoming"
    }

    section = endpoints.get(tipoBusca)
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer (seu token)"
    }
     
    url = f"https://api.themoviedb.org/3/movie/{section}?language=en-US&page=1"
    
    try:
        response = requests.get(url, headers=headers)
        
        response.raise_for_status()
        
        resposta = response.json()
        
        for film in resposta["results"]:
            nome = film.get("title")
            data = film.get("release_date")
            nota = film.get("vote_average")
            print (f"Nome:  {nome}, Nota:  {nota}, Data de Lançamento:  {data}")
            
            
    except requests.exceptions.HTTPError as err:
        print(f"\n[ERRO] Falha na API do TMDB. Verifique se seu Token está correto.")
        print(f"Detalhes do erro: {err}")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um problema inesperado: {e}")    
        

def main():
    parser = argparse.ArgumentParser(
        description="tmdb-app: Um cliente de terminal para explorar filmes no TMDB."
    )

    # Define o argumento --type e restringe as opções válidas
    parser.add_argument(
        "-t", "--type",
        choices=["playing", "popular", "top", "upcoming"],
        required=True,
        help="Tipo de lista de filmes que você deseja buscar."
    )

    # Executa a leitura dos argumentos passados pelo usuário
    args = parser.parse_args()
    
    buscar_filme(args.type)
    

if __name__ == "__main__":
    main()

