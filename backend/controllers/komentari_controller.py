from typing import Annotated

from database import engine
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from services import postovi_service
from schemas.postovi_schema import KomentarCreate,KomentarRead, KomentarUpdate

def get_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/", response_model=KomentarRead)
def create_komentar(session: SessionDep, koment_data: KomentarCreate):
  return postovi_service.create_komentar(session, koment_data)

@router.get("/")
def list_koments(session: SessionDep, offset: int = 0, limit: int = 100):
  return postovi_service.get_koments(session, offset, limit)

@router.get("/{komentar_id}")
def get_komentar(session: SessionDep, koment_id: int):
  return postovi_service.get_komentar(session, koment_id)

@router.put("/{post_id}")
def update_komentar(session: SessionDep, komentar_id: int, koment_data: KomentarUpdate):
  return postovi_service.update_komentar(session, komentar_id, koment_data)

@router.delete("/{komentar_id}")
def delete_komentar(komentar_id: int, session: Session = Depends(get_session)):
    postovi_service.delete_komentar(session, komentar_id)
    return {"message": "Komentar izbrisan!"}
 
