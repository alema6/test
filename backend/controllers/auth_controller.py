from typing import Annotated
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from sqlmodel import Session
from services import user_service
from schemas.user_schema import UserCreate, UserRead, UserUpdate, UserLogin
from security import Token

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = user_service.login_user(db=db, email=user.email, password=user.password)
    return {"access_token": token, "token_type": "bearer"}

