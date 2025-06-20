from sqlmodel import SQLModel, Field
from datetime import datetime


class Razgovor(SQLModel, table = True):
    razgovor_id: int | None = Field( default = None, primary_key = True)
    tema: str

class Poruka(SQLModel, table = True):
    poruke_id: int | None = Field( default = None, primary_key = True)
    sender: int | None = Field(default = None, foreign_key = "user.id")
    receiver: int | None = Field(default = None, foreign_key = "user.id")    
    razgovor_id:  int
    tekst: str
    datum_slanja: datetime