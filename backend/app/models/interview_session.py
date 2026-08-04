from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    JSON,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class InterviewSession(Base):

    __tablename__ = "interview_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    session_name = Column(
        String(150),
        nullable=False
    )

    company_name = Column(
        String(150)
    )

    job_role = Column(
        String(150)
    )

    interview_level = Column(
        String(50),
        default="Beginner"
    )

    score = Column(
        Float,
        default=0.0
    )

    feedback = Column(
        JSON
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="interview_sessions"
    )