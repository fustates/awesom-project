from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/")
async def root():
    return {"message": "Project is running!", "tech_stack": "FastAPI + uv + Python 3.13"}