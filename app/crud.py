import uuid
from typing import Any
from sqlmodel import Session, select
from app.core import security 
from app.models import User, UserCreate


def create_user(*, session: Session, user_create: UserCreate):
    db_obj = User.model_validate(
        user_create, update={"hashed_password": security.get_password_hash(user_create.password)}
    )
    session.add(db_obj) 
    session.commit()
    session.refresh(db_obj)
    return db_obj
    
    
def get_user_by_email(*, session : Session, email : str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user

def authenticate(*, session : Session, email : str, plain_password : str):
    db_user = get_user_by_email(email)

    if not db_user:
        return None
    if not security.verify_password(plain_password, db_user.hashed_password):
        return None
    
    return db_user
    
