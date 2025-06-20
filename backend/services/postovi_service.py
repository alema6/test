from sqlmodel import Session
from schemas.postovi_schema import ObjavaCreate, ObjavaUpdate,KomentarCreate,KomentarUpdate
from models.postovi_model import Post,Komentar
from repositories import postovi_repository
from fastapi import HTTPException

def create_post(session: Session, post_data: ObjavaCreate) -> Post:
    objava = Post(**post_data.dict())
    return postovi_repository.create_post(session, objava)

def get_postove(session: Session, offset: int, limit: int) -> list[Post]:
    return postovi_repository.get_postove(session, offset, limit)

def get_post(session:Session, post_id: int) -> Post:
  objava = postovi_repository.get_post(session, post_id)

  if not objava:
    raise HTTPException(status_code=404, detail="Objava not found")
  
  return objava

def update_post(session: Session, post_id: int, post_data: ObjavaUpdate) -> Post:
  db_objava = postovi_repository.get_post(session, post_id)

  if not db_objava:
    raise HTTPException(status_code=404, detail="Objava not found")
  
  return postovi_repository.update_post(session, db_objava, post_data.dict(exclude_unset=True))

def delete_post(session: Session, post_id: int) -> None:
  db_objava = postovi_repository.get_post(session, post_id)

  if not db_objava:
    raise HTTPException(status_code=404, detail="Poruka not found")
  
  postovi_repository.delete_post(session, db_objava)


#   KOMENTARI NA OBJAVE


def create_komentar(session: Session, post_data: KomentarCreate) -> Komentar:
    koment = Komentar(**post_data.dict())
    return postovi_repository.create_komentar(session, koment)

def get_koments(session: Session, offset: int, limit: int) -> list[Komentar]:
    return postovi_repository.get_koments(session, offset, limit)

def get_komentar(session:Session, komentar_id: int) -> Komentar:
  koment = postovi_repository.get_komentar(session, komentar_id)

  if not koment:
    raise HTTPException(status_code=404, detail="Komentar not found")
  
  return koment

def update_komentar(session: Session, komentar_id: int, koment_data: KomentarUpdate) -> Komentar:
  db_koment = postovi_repository.get_komentar(session, komentar_id)

  if not db_koment:
    raise HTTPException(status_code=404, detail="Komentar not found")
  
  return postovi_repository.update_komentar(session, db_koment, koment_data.dict(exclude_unset=True))

def delete_komentar(session: Session, koment_id: int) -> None:
  db_koment = postovi_repository.get_komentar(session, koment_id)

  if not db_koment:
    raise HTTPException(status_code=404, detail="Komentar not found")
  
  postovi_repository.delete_komentar(session, db_koment)