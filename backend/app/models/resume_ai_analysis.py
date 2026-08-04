from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
    String,
    Float,
    DateTime,
    func
)

from sqlalchemy.orm import relationship


from app.core.database import Base

class ResumeAIAnalysis(Base):

    __tablename__ = "resume_ai_analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False,
        unique=True
    )

    parsed_json = Column(
        JSON,
        nullable=False
    )

    provider = Column(
        String(50),
        nullable=False,
        default="gemini"
    )

    model_name = Column(
        String(100),
        nullable=False
    )

    model_version = Column(
        String(50),
        nullable=False
    )

    processing_time = Column(
        Float,
        default=0.0
    )

    status = Column(
        String(20),
        default="SUCCESS"
    )

    error_message = Column(
        String(1000),
        nullable=True
    )

    token_usage = Column(
        Integer,
        default=0
    )

    estimated_cost = Column(
        Float,
        default=0.0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="analysis"
    )