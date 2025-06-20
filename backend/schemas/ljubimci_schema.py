from pydantic import BaseModel
from datetime import date
from typing import Optional

# Kreiranje ljubimca
class LjubimacCreate(BaseModel):
    user_id: Optional[int] = None
    ime: str
    nadimak: str
    datum_rodjenja: date
    vrsta_ljubimca: str
    rasa_ljubimca: str
    zemlja_porijekla_ljubimca: str
    boja_ljubimca: str
    opis: str
    slika: Optional[bytes] = None

# Citanje ljubimca
class LjubimacRead(BaseModel):
    ljubimci_id: int
    user_id: Optional[int] = None
    ime: str
    nadimak: str
    datum_rodjenja: date
    vrsta_ljubimca: str
    rasa_ljubimca: str
    zemlja_porijekla_ljubimca: str
    boja_ljubimca: str
    opis: str
    slika: Optional[bytes] = None

# Azuriranje ljubimca
class LjubimacUpdate(BaseModel):
    user_id: Optional[int] = None
    ime: Optional[str] = None
    nadimak: Optional[str] = None
    datum_rodjenja: Optional[date] = None
    vrsta_ljubimca: Optional[str] = None
    rasa_ljubimca: Optional[str] = None
    zemlja_porijekla_ljubimca: Optional[str] = None
    boja_ljubimca: Optional[str] = None
    opis: Optional[str] = None
    slika: Optional[bytes] = None
