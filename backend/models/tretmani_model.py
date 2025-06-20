from sqlmodel import SQLModel, Field
from datetime import date

class tretmani(SQLModel, table = True):
    tretmani_id: int | None = Field( default = None, primary_key = True)
    ljubimac_id_fr_key: int | None = Field(default = None, foreign_key = "ljubimci.ljubimci_id")
    user_id: int | None = Field(default = None, foreign_key = "user.id")
    vrsta_tretmana: str
    datum_tretmana: date
    zavrsen_tretman: bool = Field(default = False)