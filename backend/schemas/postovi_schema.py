from pydantic import BaseModel
from datetime import datetime

# Objava
class ObjavaCreate(BaseModel):
  poster: int
  tekst: str
  datum_slanja: datetime

class ObjavaRead(BaseModel):
  post_id: int
  poster: int
  tekst: str
  datum_slanja: datetime


class ObjavaUpdate(BaseModel):
  post_id:int
  poster: int
  tekst: str
  datum_slanja: datetime



# Komentar
class KomentarCreate(BaseModel):
  komentator: int
  post: int
  tekst: str
  datum_slanja: datetime

class KomentarRead(BaseModel):
  komentar_id: int
  komentator: int
  post: int
  tekst: str
  datum_slanja: datetime

class KomentarUpdate(BaseModel):
  komentar_id: int
  komentator: int
  post: int
  tekst: str
  datum_slanja: datetime