from sqlmodel import Session, select
from models.ljubimci_model import ljubimci

# CREATE
def create_ljubimac(session: Session, ljubimac: ljubimci) -> ljubimci:
    session.add(ljubimac)
    session.commit()
    session.refresh(ljubimac)
    return ljubimac

# READ - LIST
def get_ljubimci(session: Session, offset: int = 0, limit: int = 100) -> list[ljubimci]:
    return session.exec(select(ljubimci).offset(offset).limit(limit)).all()

# READ - POJEDINACNO
def get_ljubimac(session: Session, ljubimci_id: int) -> ljubimci | None:
    return session.get(ljubimci, ljubimci_id)

# UPDATE
def update_ljubimac(session: Session, db_ljubimac: ljubimci, updates: dict) -> ljubimci:
    for key, value in updates.items():
        setattr(db_ljubimac, key, value)
    session.add(db_ljubimac)
    session.commit()
    session.refresh(db_ljubimac)
    return db_ljubimac

# DELETE
def delete_ljubimac(session: Session, db_ljubimac: ljubimci) -> None:
    session.delete(db_ljubimac)
    session.commit()
