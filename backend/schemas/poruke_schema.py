from pydantic import BaseModel
from datetime import datetime

# PORUKA
class PorukaCreate(BaseModel):
  sender: int
  receiver: int
  razgovor_id:int
  tekst: str
  datum_slanja: datetime

class PorukaRead(BaseModel):
  poruke_id: int
  sender: int 
  receiver: int  
  razgovor_id:  int 
  tekst: str
  datum_slanja: datetime


class PorukaUpdate(BaseModel):
  razgovor_id:int
  tekst: str



# RAZGOVOR
class RazgovorCreate(BaseModel):
  tema: str

class RazgovorRead(BaseModel):
  razgovor_id: int
  tema: str

class RazgovorUpdate(BaseModel):
  tema: str