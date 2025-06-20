
from typing import Annotated

from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from services import poruke_service
from schemas.poruke_schema import PorukaCreate, PorukaRead, PorukaUpdate, RazgovorCreate, RazgovorRead, RazgovorUpdate

def get_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

# PORUKA

@router.post("/", response_model=PorukaRead)
def create_poruka(session: SessionDep, poruka_data: PorukaCreate):
  return poruke_service.create_poruka(session, poruka_data)

@router.get("/")
def list_poruke(session: SessionDep, offset: int = 0, limit: int = 100):
  return poruke_service.get_poruke(session, offset, limit)

@router.get("/{poruka_id}")
def get_poruka(session: SessionDep, poruka_id: int):
  return poruke_service.get_poruka(session, poruka_id)

@router.put("/{poruka_id}")
def update_poruka(session: SessionDep, poruka_id: int, poruka_data: PorukaUpdate):
  return poruke_service.update_poruka(session, poruka_id, poruka_data)

@router.delete("/{poruka_id}")
def delete_poruka(poruka_id: int, session: Session = Depends(get_session)):
  poruke_service.delete_poruka(session, poruka_id)
 
  return {"message": "Poruka izbrisansa!"}