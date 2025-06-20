from sqlmodel import Session, select
from models.postovi_model import Post,Komentar

def create_post(session: Session, objava: Post) ->  Post:
  session.add(objava)
  session.commit()
  session.refresh(objava)

  return objava

def get_postove(session:Session, offset: int = 0, limit: int = 100) -> list[Post]:
  return session.exec(select(Post).offset(offset).limit(limit)).all()

def get_post(session: Session, post_id: int) -> Post | None:
  return session.get(Post, post_id)

def update_post(session:Session, db_post: Post, updates: dict) -> Post:
  for key, value in updates.items():
    setattr(db_post, key, value)

  session.add(db_post)
  session.commit()
  session.refresh(db_post)

  return db_post

def delete_post(session: Session, db_post: Post)  -> None:
  session.delete(db_post)
  session.commit()


# KOMENTAR NA POST
def create_komentar(session: Session, komentar: Komentar) ->  Komentar:
  session.add(komentar)
  session.commit()
  session.refresh(komentar)

  return komentar

def get_koments(session:Session, offset: int = 0, limit: int = 100) -> list[Komentar]:
  return session.exec(select(Komentar).offset(offset).limit(limit)).all()

def get_komentar(session: Session, komentar_id: int) -> Komentar | None:
  return session.get(Komentar, komentar_id)

def update_komentar(session:Session, db_koment: Komentar, updates: dict) -> Komentar:
  for key, value in updates.items():
    setattr(db_koment, key, value)

  session.add(db_koment)
  session.commit()
  session.refresh(db_koment)

  return db_koment

def delete_komentar(session: Session, db_koment: Komentar)  -> None:
  session.delete(db_koment) 
  session.commit()