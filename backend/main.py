from contextlib import asynccontextmanager
from typing import Annotated

from database import engine, Base
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from controllers import user_controller,poruke_controller,razgovor_controller,komentari_controller,postovi_controller, auth_controller, ljubimci_controller, tretmani_controller
from starlette.middleware.cors import CORSMiddleware

from models.user_model import User, RoleEnum
from security import get_password_hash

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)
  # Dodaj admina ako ne postoji
  with Session(engine) as session:
    admin_email = "admin@site.com"
    existing_admin = session.exec(select(User).where(User.email == admin_email)).first()
    if not existing_admin:
      admin = User(
        username="admin",
        email=admin_email,
        hashed_password=get_password_hash("admin123"),
        naziv_ime="Administrator",
        adresa="Adminova Ulica 1",
        broj="000-000",
        role="admin",
        odobren=True,
      )
      session.add(admin)
      session.commit()
      print("✅ Admin korisnik kreiran.")

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_tables()
  yield
  print("Gašenje aplikacije")

#veza front-back
def start_application():
  app = FastAPI(lifespan=lifespan)
  
  origins = ["*"] #ovdje idu IP adrese koje će imati pristup backu
  
  app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
  )

  return app


app = start_application()

app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(poruke_controller.router, prefix="/poruke", tags=["Poruke"])
app.include_router(razgovor_controller.router, prefix="/razgovor", tags=["Razgovori"])
app.include_router(postovi_controller.router, prefix="/objava", tags=["Objave"])
app.include_router(komentari_controller.router, prefix="/komentar", tags=["Komentar"])
app.include_router(ljubimci_controller.router, prefix="/ljubimci", tags=["Ljubimci"])
app.include_router(tretmani_controller.router, prefix="/tretmani", tags=["Tretmani"])

app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])