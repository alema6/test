from sqlmodel import Session, select
from schemas.user_schema import UserCreate, UserUpdate 
from models.user_model import User
from repositories import user_repository
from repositories.user_repository import get_user_by_email
from security import verify_password, create_access_token, get_password_hash
from fastapi import HTTPException, status

def register_user(db: Session, user: UserCreate):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    user_dict = user.dict()
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))

    # Odobreni odmah ako je obični user
    user_dict["odobren"] = user.role == "user"

    new_user = User(**user_dict)
    return user_repository.create_user(db, new_user)

def login_user(db: Session, email: str, password: str):
  db_user = get_user_by_email(db, email=email)
  if not db_user or not verify_password(password, db_user.hashed_password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
  if not db_user.odobren:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Vaš nalog još nije odobren od strane administratora.")
  return create_access_token(data={"sub": db_user.email, "role": db_user.role})


def create_user(session: Session, user_data: UserCreate) -> User:
  #user = User(**user_data.dict())
  #return user_repository.create_user(session, user)
  user_dict = user_data.dict()
  # Hash the plain password before creating the user
  user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
  user = User(**user_dict)
  return user_repository.create_user(session, user)

def get_users(session: Session, offset: int, limit: int) -> list[User]:
  return user_repository.get_users(session, offset, limit)

def get_user(session:Session, user_id: int) -> User:
  user = user_repository.get_user(session, user_id)

  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  
  return user

def update_user(session: Session, user_id: int, user_data: UserUpdate) -> User:
  db_user = user_repository.get_user(session, user_id)

  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")
    
  updates = user_data.dict(exclude_unset=True)
  if "password" in updates:
    updates["hashed_password"] = get_password_hash(updates.pop("password"))
    
  return user_repository.update_user(session, db_user, updates)

def delete_user(session: Session, user_id: int) -> None:
  db_user = user_repository.get_user(session, user_id)

  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")
  
  user_repository.delete_user(session, db_user)

def get_users_na_odobrenje(session: Session) -> list[User]:
  statement = select(User).where(User.odobren == False, User.role != "user")
  return session.exec(statement).all()

def odobri_user(session: Session, user_id: int) -> User:
  user = user_repository.get_user(session, user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  if user.role == "user":
    raise HTTPException(status_code=400, detail="Obični korisnik ne zahteva odobrenje")

  user.odobren = True
  return user_repository.update_user(session, user, {"odobren": True})  