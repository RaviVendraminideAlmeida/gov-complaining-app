from fastapi import APIRouter, Depends, HTTPException

from app.models import Complaint, ComplaintsPublic, ComplaintPublic
from app.api.deps import SessionDep
from typing import Any
from sqlmodel import func, select


router = APIRouter(prefix="/complaints", tags=["complaints"])


@router.get("/", response_model=ComplaintsPublic)
def get_complaints(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100
) -> Any:
    """ 
     Retrieve all complaints
    """
    count_statement = select(func.count()).select_from(Complaint)
    count = session.exec(count_statement).one()
    statement = select(Complaint).offset(skip).limit(limit)
    items = session.exec(statement).all()
 
    return ComplaintsPublic(count=count, data=items)



