import requests
from fastapi import FastAPI
import dotenv
import os
from pycine.models import *

# carrega o arquivo .env
dotenv.load_dotenv(".env") 
# busca pela variavel de ambiente
token = os.environ["API_TOKEN"] 

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

#fastapi() deve rodar em apenas um lugar, foi escolhido deixar rodar na main
#app = FastAPI()

#@app.get("/")
#def root():
#    return { "status": "up and running" }

#exemplo passado anteriormente, será feito um novo abaixo
#@app.get("/movies1") # http :8000/movies
def get_movies1():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=vote_count.desc&primary_release_year=2010"
    data = get_json(url)
    results = data['results']
    titles = []  # inicializa a lista
    for mov in results:
        titles.append(
            { 
                'title': mov['title'], 
                'release': mov['release_date'] 
            }
        )  
    return titles
#NOVO
#@app.get("/movie/{id}")
def get_movie(id: int):
    #obtem o filme pelo id
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    data = get_json(url)
    movie = Movie.model_validate(data)
    return movie

def search_movie(params: dict = None):
    #busca filmes usando filtros
    url = "https://api.themoviedb.org/3/discover/movie"
    params = params or {
        "include_adult":False,
        "include_video":False,
        "language":"en-US",
        "page": 1,
        "sort_by":"popularity.desc"
    }
    search_result = get_json(url, params)
    return MovieResults.model_validate(search_result)

def top_movies():
    #retorna uma lista dos melhores filmes de todos os tempos
    url = "https://api.themoviedb.org/3/movie/top_rated"
    top = get_json(url)
    return MoviesResults.model_validate(top)
    


#@app.get("/generos")
def get_genres():  # (3)
    """ 
    endpoint: https://api.themoviedb.org/3/genre/movie/list
    lista todos os generos (tipos de filmes) disponíveis no tmdb 
    """
    url = "https://api.themoviedb.org/3/genre/movie/list"
    return get_json(url)

# (1) localhost:8000/artista/arnold
# (2) localhost:8000/artista?nome=arnold
#@app.get("/artista/{nome}") # (1)
def search_person(name: str):
    url = f"https://api.themoviedb.org/3/search/person?query={name}&include_adult=false&language=en-US&page=1"
    person = get_json(url)
    return NamePerson.model_validate(person)

def id_person(id: int):
    url = f"https://api.themoviedb.org/3/person/{id}?language=en-US"
    id_person = get_json(url)
    return Person.model_validate(id_person)

def popular_person():
    url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"
    p_person = get_json(url)
    return NamePerson.model_validate(p_person)

def movies_person(id: int):
    url = f"https://api.themoviedb.org/3/person/{id}/movie_credits?language=en-US"
    movies_person = get_json(url)
    return PersonMovies.model_validate(movies_person)

def trending_person(period: str):
    url = f"https://api.themoviedb.org/3/trending/person/{period}?language=en-US"
    t_person = get_json(url)
    #return t_person
    return TrendingPerson.model_validate(t_person)


def get_movie1(title: str): # (2)
    """ 
    Procura um filme pelo titulo. Retorna os seguintes campos:
    "id"
    "title"
    "genres"
    "original_language"
    "overview"
    "popularity"
    "poster_path"
    "release_date"
    "vote_count"
    """
    ...

def get_elenco(movie_id: int): # (4)
    """ 
    Lista dos artistas que participaram no filme.
    Retorna id e nome para cada artista
    """
    ...


