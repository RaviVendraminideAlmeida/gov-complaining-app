from fastapi import FastAPI
from app.api.main import api_router
from fastapi.routing import APIRoute

app = FastAPI(title="TODO: MOVE THIS TO AN EXTERNAL CONFIG FILE")

app.include_router(api_router)
