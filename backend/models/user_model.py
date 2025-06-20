from sqlmodel import SQLModel, Field
import enum

class RoleEnum(str, enum.Enum):
    user = "user"
    shelter = "shelter"
    healthcare = "healthcare"
    admin = "admin"

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    naziv_ime: str | None = None
    adresa: str | None = None
    broj: str | None = None
    role: RoleEnum = Field(default=RoleEnum.user, sa_column_kwargs={"nullable": False})
    odobren: bool = Field (default=True)