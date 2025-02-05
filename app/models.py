import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class UserBase(SQLModel):
    email : EmailStr = Field(unique=True, index=True, max_length=255)
    is_active : bool = True
    is_superuser : bool = False
    full_name : str | None = Field(default=None, max_length=255)

class UserCreate(UserBase):
    password : str = Field(min_length=8, max_length=40)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password : str
    complaints : list["Complaint"] = Relationship(back_populates="author", cascade_delete=True)
 
class UsersPublic(SQLModel): 
    data: list[UserBase]
    count: int
  
class ComplaintBase(SQLModel):
    title : str | None = Field(min_length=3, max_length=255)
    content : str | None = Field(default=None, max_length=255)
    
class Complaint(ComplaintBase, table=True):
    id : uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title : str = Field(max_length=512)
    author_id : uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    author : User | None = Relationship(back_populates="complaints")

class ComplaintPublic(ComplaintBase):
    id: uuid.UUID | None
    author_id: uuid.UUID
    
class ComplaintsPublic(SQLModel):
    data : list[ComplaintPublic]
    count : int
    