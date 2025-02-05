from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import SessionDep
from sqlmodel import func, select
from app.models import User, UsersPublic, UserCreate
from app.core.config import settings

from app import crud, utils

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100
):
    """
        Retrieve users
    """
    count_statement = select(func.count()).select_from(User)
    count = session.exec(count_statement).one()
    statement = select(User).offset(skip).limit(limit)
    items = session.exec(statement).all()

    return UsersPublic(data=items, count=count)


@router.post("/")
async def create_user(
    *,
    session: SessionDep,
    user_in: UserCreate
):
    """
        Create new user
    """
    user = crud.get_user_by_email(session=session, email=user_in.email)

    if user:
        raise HTTPException(
            status_code=400,
            detail="Já existe um usuário com esse e-mail no sistema."
        )

    user = crud.create_user(session=session, user_create=user_in)

    """
        TODO: Implement e-mail verification 
    """
    
    return user