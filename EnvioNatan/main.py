from fastapi import FastAPI
from typing import Union
from pycine import models
from fastapi.middleware.cors import CORSMiddleware
import pycine.tmdb as tmdb
import os
import dotenv
import motor.motor_asyncio

dotenv.load_dotenv(".env") 
db_url = os.environ["MONGODB_URL"] 


app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
db= client.pycine

origins = [
    "http://localhost",
    "http://localhost:*",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "pycine is runing"}

@app.get("/movie/{id}")
def get_movie(id: int):
    return tmdb.get_movie(id)

@app.get("/find/",
    response_description="List all movies",
    response_model=models.MovieResults,
    response_model_by_alias=False,
)
async def list_movies():
    movies_collection = db.get_collection("movie")
    return models.MovieResults(
        movies=await movies_collection.find().to_list(20)
    )


@app.get("/search/movie")
def search_movie():
    return tmdb.search_movie()

@app.get("/top/movies")
def top_movie():
    return tmdb.top_movies()

@app.get("/person/{name}")
def search_person(name: str):
    return tmdb.search_person(name)

@app.get("/id_person/{id}")
def id_person(id: int):
    return tmdb.id_person(id)

@app.get("/popular_person")
def popular_person():
    return tmdb.popular_person()

@app.get("/movies_person/{id}")
def movies_person(id: int):
    return tmdb.movies_person(id)

@app.get("/trending/person/{period}")
def trending_person(period: str):
    return tmdb.trending_person(period)

