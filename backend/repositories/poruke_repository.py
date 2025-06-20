from sqlmodel import Session, select
from models.poruke_model import Poruka,Razgovor

# PORUKA #
def create_poruka(session: Session, poruka: Poruka) ->  Poruka:
  session.add(poruka)
  session.commit()
  session.refresh(poruka)

  return poruka

def get_poruke(session:Session, offset: int = 0, limit: int = 100) -> list[Poruka]:
  return session.exec(select(Poruka).offset(offset).limit(limit)).all()

def get_poruka(session: Session, poruka_id: int) -> Poruka | None:
  return session.get(Poruka, poruka_id)

def update_poruka(session:Session, db_poruka: Poruka, updates: dict) -> Poruka:
  for key, value in updates.items():
    setattr(db_poruka, key, value)

  session.add(db_poruka)
  session.commit()
  session.refresh(db_poruka)

  return db_poruka

def delete_poruka(session: Session, db_poruka: Poruka)  -> None:
  session.delete(db_poruka)
  session.commit()


#  RAZGOVOR  #

def create_razgovor(session: Session, razg: Razgovor) ->  Razgovor:
  session.add(razg)
  session.commit()
  session.refresh(razg)
  return razg


def get_razgovore(session:Session, offset: int = 0, limit: int = 100) -> list[Razgovor]:
  return session.exec(select(Razgovor).offset(offset).limit(limit)).all()

def get_razgovor(session: Session, razgovor_id: int) -> Razgovor | None:
  return session.get(Razgovor, razgovor_id)

def update_razgovor(session:Session, db_razg: Razgovor, updates: dict) -> Razgovor:
  for key, value in updates.items():
    setattr(db_razg, key, value)

  session.add(db_razg)
  session.commit()
  session.refresh(db_razg)
  return db_razg

def delete_razgovor(session: Session, db_razg: Razgovor)  -> None:
  session.delete(db_razg)
  session.commit()