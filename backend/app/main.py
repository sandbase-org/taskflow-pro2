from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
from app.database import engine
from app.models import Base  # type: ignore

app = FastAPI(title=settings.PROJECT_NAME)

# Create tables (for dev; use alembic in prod)
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow Pro"}