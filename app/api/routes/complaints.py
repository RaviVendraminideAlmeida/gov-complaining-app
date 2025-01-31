from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/complaints", tags=["complaints"])


@router.get("/")
async def get_complaints():
    return [{"text": "Lorem Ipsum Dolor Sit Amet"}]
