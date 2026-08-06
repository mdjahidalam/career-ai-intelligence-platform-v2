from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.exceptions import register_exception_handlers

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.resume import router as resume_router
from app.core.database import Base, engine
from app.models.user import User
from app.models.resume import Resume
from app.models.resume_ai_analysis import ResumeAIAnalysis

from app.models.resume_version import ResumeVersion
from app.models.job import Job
from app.models.job_matching import JobMatching
from app.models.career_path import CareerPath
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage
from app.models.interview_session import InterviewSession
from app.models.notification import Notification
from app.models.skill import Skill



app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG,
)

Base.metadata.create_all(bind=engine)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

# Future
# app.include_router(job_router)
# app.include_router(career_router)
# app.include_router(chat_router)
# app.include_router(interview_router)
# app.include_router(notification_router)