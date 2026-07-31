from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
    DateTime,
    String
)

from sqlalchemy.sql import func
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
        nullable=False
    )

    # Complete AI Analysis JSON
    parsed_json = Column(
        JSON,
        nullable=False
    )

    # AI Model Information
    model_name = Column(
        String(100),
        nullable=False
    )

    model_version = Column(
        String(50),
        nullable=False
    )

    # Created Time
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="analysis"
    )