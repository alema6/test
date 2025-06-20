from sqlmodel import Session
from schemas.poruke_schema import PorukaCreate, PorukaUpdate, RazgovorCreate, RazgovorUpdate
from models.poruke_model import Poruka,Razgovor
from repositories import poruke_repository
from fastapi import HTTPException


# PORUKE
def create_poruka(session: Session, poruka_data: PorukaCreate) -> Poruka:
    poruka = Poruka(**poruka_data.dict())
    return poruke_repository.create_poruka(session, poruka)

def get_poruke(session: Session, offset: int, limit: int) -> list[Poruka]:
    return poruke_repository.get_poruke(session, offset, limit)

def get_poruka(session:Session, poruka_id: int) -> Poruka:
  poruka = poruke_repository.get_poruka(session, poruka_id)

  if not poruka:
    raise HTTPException(status_code=404, detail="Poruka not found")
  
  return poruka

def update_poruka(session: Session, poruka_id: int, poruka_data: PorukaUpdate) -> Poruka:
  db_poruka = poruke_repository.get_poruka(session, poruka_id)

  if not db_poruka:
    raise HTTPException(status_code=404, detail="Poruka not found")
  
  return poruke_repository.update_poruka(session, db_poruka, poruka_data.dict(exclude_unset=True))

def delete_poruka(session: Session, poruka_id: int) -> None:
  db_poruka = poruke_repository.get_poruka(session, poruka_id)

  if not db_poruka:
    raise HTTPException(status_code=404, detail="Poruka not found")
  
  poruke_repository.delete_poruka(session, db_poruka)


# RAZGOVORI


def create_razgovor(session: Session, razg_data: RazgovorCreate) -> Razgovor:
    razg = Razgovor(**razg_data.dict())
    return poruke_repository.create_razgovor(session, razg)

def get_razgovore(session: Session, offset: int, limit: int) -> list[Razgovor]:
    return poruke_repository.get_razgovore(session, offset, limit)

def get_razgovor(session:Session, razgovor_id: int) -> Razgovor:
  razg = poruke_repository.get_razgovor(session, razgovor_id)

  if not razg:
    raise HTTPException(status_code=404, detail="Razgovor ne postoji pod tim id-om")
  
  return razg

def update_razgovor(session: Session, razgovor_id: int, razgovor_data: RazgovorUpdate) -> Razgovor:
  db_razg = poruke_repository.get_razgovor(session, razgovor_id)

  if not db_razg:
    raise HTTPException(status_code=404, detail="Razgovor ne postoji pod tim id-om")
  
  return poruke_repository.update_razgovor(session, db_razg, razgovor_data.dict(exclude_unset=True))

def delete_razgovor(session: Session, razgovor_id: int) -> None:
  db_razg = poruke_repository.get_razgovor(session, razgovor_id)

  if not db_razg:
    raise HTTPException(status_code=404, detail="Razgovor ne postoji pod tim id-om")
  
  poruke_repository.delete_razgovor(session, db_razg)