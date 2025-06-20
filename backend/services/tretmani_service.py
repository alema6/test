from sqlmodel import Session
from fastapi import HTTPException, status
from schemas.tretmani_schema import TretmanCreate, TretmanUpdate
from models.tretmani_model import tretmani
from repositories import tretmani_repository


def create_tretman(session: Session, tretman_data: TretmanCreate) -> tretmani:
    tretman = tretmani(**tretman_data.dict())
    return tretmani_repository.create_tretman(session, tretman)


def get_svi_tretmani(session: Session, offset: int = 0, limit: int = 100) -> list[tretmani]:
    return tretmani_repository.get_svi_tretmani(session, offset, limit)


def get_tretman(session: Session, tretman_id: int) -> tretmani:
    tretman = tretmani_repository.get_tretman(session, tretman_id)
    if not tretman:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tretman nije pronađen")
    return tretman


def update_tretman(session: Session, tretman_id: int, tretman_data: TretmanUpdate) -> tretmani:
    db_tretman = tretmani_repository.get_tretman(session, tretman_id)
    if not db_tretman:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tretman nije pronađen")

    updates = tretman_data.dict(exclude_unset=True)
    return tretmani_repository.update_tretman(session, db_tretman, updates)


def delete_tretman(session: Session, tretman_id: int) -> None:
    db_tretman = tretmani_repository.get_tretman(session, tretman_id)
    if not db_tretman:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tretman nije pronađen")
    tretmani_repository.delete_tretman(session, db_tretman)
