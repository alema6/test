from sqlmodel import Session
from fastapi import HTTPException, status
from schemas.ljubimci_schema import LjubimacCreate, LjubimacUpdate
from models.ljubimci_model import ljubimci
from repositories import ljubimci_repository


def create_ljubimac(session: Session, ljubimac_data: LjubimacCreate) -> ljubimci:
    ljubimac = ljubimci(**ljubimac_data.dict())
    return ljubimci_repository.create_ljubimac(session, ljubimac)


def get_ljubimci(session: Session, offset: int = 0, limit: int = 100) -> list[ljubimci]:
    return ljubimci_repository.get_ljubimci(session, offset, limit)


def get_ljubimac(session: Session, ljubimac_id: int) -> ljubimci:
    ljubimac = ljubimci_repository.get_ljubimac(session, ljubimac_id)
    if not ljubimac:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ljubimac nije pronađen")
    return ljubimac


def update_ljubimac(session: Session, ljubimac_id: int, ljubimac_data: LjubimacUpdate) -> ljubimci:
    db_ljubimac = ljubimci_repository.get_ljubimac(session, ljubimac_id)
    if not db_ljubimac:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ljubimac nije pronađen")

    updates = ljubimac_data.dict(exclude_unset=True)
    return ljubimci_repository.update_ljubimac(session, db_ljubimac, updates)


def delete_ljubimac(session: Session, ljubimac_id: int) -> None:
    db_ljubimac = ljubimci_repository.get_ljubimac(session, ljubimac_id)
    if not db_ljubimac:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ljubimac nije pronađen")
    ljubimci_repository.delete_ljubimac(session, db_ljubimac)
