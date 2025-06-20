from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import engine
from schemas.ljubimci_schema import LjubimacCreate, LjubimacRead, LjubimacUpdate
from services import ljubimci_service


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

# Router za ljubimce
router = APIRouter(prefix="/ljubimci", tags=["Ljubimci"])

@router.post("/", response_model=LjubimacRead)
def create_ljubimac(session: SessionDep, ljubimac_data: LjubimacCreate):
    return ljubimci_service.create_ljubimac(session, ljubimac_data)

@router.get("/", response_model=list[LjubimacRead])
def list_ljubimci(session: SessionDep, offset: int = 0, limit: int = 100):
    return ljubimci_service.get_ljubimci(session, offset, limit)

@router.get("/{ljubimac_id}", response_model=LjubimacRead)
def get_ljubimac(session: SessionDep, ljubimac_id: int):
    return ljubimci_service.get_ljubimac(session, ljubimac_id)

@router.put("/{ljubimac_id}", response_model=LjubimacRead)
def update_ljubimac(session: SessionDep, ljubimac_id: int, ljubimac_data: LjubimacUpdate):
    return ljubimci_service.update_ljubimac(session, ljubimac_id, ljubimac_data)

@router.delete("/{ljubimac_id}")
def delete_ljubimac(session: SessionDep, ljubimac_id: int):
    ljubimci_service.delete_ljubimac(session, ljubimac_id)
    return {"message": "Ljubimac je izbrisan!"}
