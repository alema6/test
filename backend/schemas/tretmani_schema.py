from pydantic import BaseModel
from datetime import date
from typing import Optional

class TretmanCreate(BaseModel):
    ljubimac_id_fr_key: Optional[int] = None
    user_id_fr_key: Optional[int] = None
    vrsta_tretmana: str
    datum_tretmana: date
    zavrsen_tretman: Optional[bool] = False


class TretmanRead(BaseModel):
    tretmani_id: int
    ljubimac_id_fr_key: Optional[int] = None
    user_id_fr_key: Optional[int] = None
    vrsta_tretmana: str
    datum_tretmana: date
    zavrsen_tretman: bool

class TretmanUpdate(BaseModel):
    ljubimac_id_fr_key: Optional[int] = None
    user_id_fr_key: Optional[int] = None
    vrsta_tretmana: Optional[str] = None
    datum_tretmana: Optional[date] = None
    zavrsen_tretman: Optional[bool] = None