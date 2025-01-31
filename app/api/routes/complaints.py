from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/complaints", tags=["complaints"])


@router.get("/")
def get_users():
    return [{"text": "Lorem Ipsum Dolor Sit Amet"}]
