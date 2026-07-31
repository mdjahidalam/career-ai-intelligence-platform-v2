from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.api.auth import router as auth_router

from app.core.database import Base, engine
from app.models.user import User

from app.core.exceptions import register_exception_handlers
from app.api.resume import router as resume_router
from app.models.resume_ai_analysis import ResumeAIAnalysis

from app.models.resume import Resume
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG,
)
register_exception_handlers(app)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "version": settings.PROJECT_VERSION,
        "status": "running",
    }


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(resume_router)