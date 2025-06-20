from sqlmodel import SQLModel, Field
from datetime import datetime

class Post(SQLModel, table = True):
    post_id: int | None = Field( default = None, primary_key = True)
    poster: int | None = Field(default = None, foreign_key = "user.id") 
    tekst: str
    datum_slanja: datetime


class Komentar(SQLModel, table = True):
    komentar_id: int | None = Field( default = None, primary_key = True)
    komentator: int | None = Field(default = None, foreign_key = "user.id")
    post: int | None = Field(default = None, foreign_key = "post.post_id")    
    tekst: str
    datum_slanja: datetime