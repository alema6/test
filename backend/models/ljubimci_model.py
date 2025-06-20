from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class ljubimci(SQLModel, table=True):
    ljubimci_id: int | None = Field(default = None, primary_key = True)
    user_id: int | None = Field(default = None, foreign_key = "user.id")
    ime: str
    nadimak: str
    datum_rodjenja: date
    vrsta_ljubimca: str
    rasa_ljubimca:str
    zemlja_porijekla_ljubimca:str 
    boja_ljubimca:str
    slika: Optional[bytes] = None
    opis: str
