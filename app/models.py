import uuid

from sqlmodel import Field, Relationship, SQLModel

class UserBase(SQLModel):
    is_active : bool = True
    is_superuser : bool = False
    full_name : str | None = Field(default=None, max_length=255)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password : str
    complaints : list["Complaint"] = Relationship(back_populates="author", cascade_delete=True)
  
class ComplaintBase(SQLModel):
    title : str = Field(min_length=3, max_length=255)
    content : str | None = Field(default=None, max_length=255)
    
class Complaint(ComplaintBase, table=True):
    id : uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title : str = Field(max_length=512)
    author_id : uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    author : User | None = Relationship(back_populates="")
    