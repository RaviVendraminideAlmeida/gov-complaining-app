from fastapi import APIRouter, Depends
from app.api.deps import SessionDep 
from app.
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated, Any 


router = APIRouter(tags=["auth"])

@router.post("/login/access-token")
def login_acess_token(
    session : SessionDep,
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Any:
    """
        OAuth2 compatible token login, get an access token for future requests
    """
    pass