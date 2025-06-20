from sqlmodel import Session, select
from models.tretmani_model import tretmani


def create_tretman(session: Session, tretman: tretmani) -> tretmani:
    session.add(tretman)
    session.commit()
    session.refresh(tretman)
    return tretman


def get_svi_tretmani(session: Session, offset: int = 0, limit: int = 100) -> list[tretmani]:
    return session.exec(select(tretmani).offset(offset).limit(limit)).all()


def get_tretman(session: Session, tretmani_id: int) -> tretmani | None:
    return session.get(tretmani, tretmani_id)


def update_tretman(session: Session, db_tretman: tretmani, updates: dict) -> tretmani:
    for key, value in updates.items():
        setattr(db_tretman, key, value)
    session.add(db_tretman)
    session.commit()
    session.refresh(db_tretman)
    return db_tretman


def delete_tretman(session: Session, db_tretman: tretmani) -> None:
    session.delete(db_tretman)
    session.commit()
