from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class RoleEnum(str, Enum):
    user = "user"
    shelter = "shelter"
    healthcare = "healthcare"
    admin ="admin"

class UserCreate(BaseModel):
  username: str
  password: str
  email: EmailStr
  naziv_ime: str
  adresa: str
  broj: str
  role: RoleEnum
   

class UserRead(BaseModel):
  id: int
  username: str
  email: EmailStr
  naziv_ime: str
  adresa: str
  broj: str
  role: RoleEnum

  class Config:
    from_attributes = True
    
class UserUpdate(BaseModel):
  username: Optional[str] = None
  password: Optional[str] = None
  email: Optional[EmailStr] = None
  naziv_ime: Optional[str] = None
  adresa: Optional[str] = None
  broj: Optional[str] = None
  role: Optional[RoleEnum] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str