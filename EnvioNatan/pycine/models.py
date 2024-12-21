from typing import Optional, List
from bson import ObjectId
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
PyObjectId = Annotated[str, BeforeValidator(str)]

class Movie(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    genres: Optional[list] = None
    original_language: str
    overview: str
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    release_date: str
    vote_count: Optional[int] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class MovieResults(BaseModel):
    movies: list[Movie]

class MoviesResults(BaseModel):
    results: list[Movie]    
    total_pages: int
    total_results: int

class PersonMovies(BaseModel):
    cast: list[Movie]

class Person(BaseModel):
    id: int
    name: str
    popularity: Optional[float] = None
    profile_path: Optional[str] = None
    known_for_department: Optional [str] = None

class NamePerson(BaseModel):
    page: int
    results: list[Person]
    total_pages: int
    total_results: int

class TrendingPerson(BaseModel):
    results: list[Person]