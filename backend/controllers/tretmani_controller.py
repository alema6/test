from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import engine
from schemas.tretmani_schema import TretmanCreate, TretmanRead, TretmanUpdate
from services import tretmani_service


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/tretmani", tags=["Tretmani"])

@router.post("/", response_model=TretmanRead)
def create_tretman(session: SessionDep, tretman_data: TretmanCreate):
    return tretmani_service.create_tretman(session, tretman_data)

@router.get("/", response_model=list[TretmanRead])
def list_tretmani(session: SessionDep, offset: int = 0, limit: int = 100):
    return tretmani_service.get_svi_tretmani(session, offset, limit)

@router.get("/{tretman_id}", response_model=TretmanRead)
def get_tretman(session: SessionDep, tretman_id: int):
    return tretmani_service.get_tretman(session, tretman_id)

@router.put("/{tretman_id}", response_model=TretmanRead)
def update_tretman(session: SessionDep, tretman_id: int, tretman_data: TretmanUpdate):
    return tretmani_service.update_tretman(session, tretman_id, tretman_data)

@router.delete("/{tretman_id}")
def delete_tretman(session: SessionDep, tretman_id: int):
    tretmani_service.delete_tretman(session, tretman_id)
    return {"message": "Tretman je izbrisan!"}
