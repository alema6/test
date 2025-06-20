
from typing import Annotated

from database import engine
from fastapi import Depends, APIRouter
from sqlmodel import Session
from services import poruke_service
from schemas.poruke_schema import RazgovorCreate, RazgovorRead, RazgovorUpdate

def get_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

# RAZGOVOR
@router.post("/", response_model=RazgovorRead)
def create_razgovor(session: SessionDep, razg_data: RazgovorCreate):
  return poruke_service.create_razgovor(session, razg_data)

@router.get("/")
def list_razgovori(session: SessionDep, offset: int = 0, limit: int = 100):
  return poruke_service.get_razgovore(session, offset, limit)

@router.get("/{razgovor_id}")
def get_razgovor(session: SessionDep, razgovor_id: int):
  return poruke_service.get_razgovor(session, razgovor_id)

@router.put("/{razgovor_id}")
def update_razgovor(session: SessionDep, razgovor_id: int, razgovor_data: RazgovorUpdate):
  return poruke_service.update_razgovor(session, razgovor_id, razgovor_data)

@router.delete("/{razgovor_id}")
def delete_razgovor(razgovor_id: int, session: Session = Depends(get_session)):
  poruke_service.delete_razgovor(session, razgovor_id)
 
  return {"message": "Razgovor izbrisan!"}
