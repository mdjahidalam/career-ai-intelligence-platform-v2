from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False  
    )

    original_filename = Column(String(255), nullable=False)

    stored_filename = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    file_size = Column(Integer)

    file_type = Column(String(20))

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User", back_populates="resumes")
    analysis = relationship(
    "ResumeAIAnalysis",
    back_populates="resume",
    uselist=False,
    cascade="all, delete-orphan")

    versions = relationship(
    "ResumeVersion",
    back_populates="resume",
    cascade="all, delete-orphan"
    )

    job_matches = relationship(
    "JobMatching",
    back_populates="resume",
    cascade="all, delete-orphan"
    )

    career_paths = relationship(
    "CareerPath",
    back_populates="resume",
    cascade="all, delete-orphan"
    )
    
    interview_sessions = relationship(
    "InterviewSession",
    back_populates="resume",
    cascade="all, delete-orphan"
    )
    skills = relationship(
    "Skill",
    back_populates="resume",
    cascade="all, delete-orphan"
    )