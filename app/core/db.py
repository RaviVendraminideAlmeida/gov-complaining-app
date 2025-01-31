from sqlmodel import Session, create_engine, select

from app.core.config import settings
from app.models import User, Complaint

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))