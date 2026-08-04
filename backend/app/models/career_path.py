from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    JSON,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class CareerPath(Base):

    __tablename__ = "career_paths"

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

    career_title = Column(
        String(150),
        nullable=False
    )

    match_score = Column(
        Float,
        nullable=False
    )

    roadmap = Column(
        JSON,
        nullable=False
    )

    required_skills = Column(
        JSON
    )

    estimated_salary = Column(
        String(100)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="career_paths"
    )