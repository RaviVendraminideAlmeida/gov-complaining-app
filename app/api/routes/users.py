from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_users():
    return [{"name": "John Doe"}]
