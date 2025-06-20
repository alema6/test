from typing import Annotated

from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from services import postovi_service
from schemas.postovi_schema import ObjavaCreate, ObjavaRead, ObjavaUpdate

def get_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/", response_model=ObjavaRead)
def create_postovi(session: SessionDep, postovi_data: ObjavaCreate):
  return postovi_service.create_post(session, postovi_data)

@router.get("/")
def list_postovi(session: SessionDep, offset: int = 0, limit: int = 100):
  return postovi_service.get_postove(session, offset, limit)

@router.get("/{post_id}")
def get_postovi(session: SessionDep, post_id: int):
  return postovi_service.get_post(session, post_id)

@router.put("/{post_id}")
def update_postovi(session: SessionDep, post_id: int, postovi_data: ObjavaUpdate):
  return postovi_service.update_post(session, post_id, postovi_data)

@router.delete("/{post_id}")
def delete_postovi(post_id: int, session: Session = Depends(get_session)):
    postovi_service.delete_post(session, post_id)
    return {"message": "Objava izbrisana!"}
 


 