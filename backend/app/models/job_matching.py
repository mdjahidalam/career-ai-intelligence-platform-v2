from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    JSON,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class JobMatching(Base):

    __tablename__ = "job_matching"

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

    job_id = Column(
        Integer,
        ForeignKey(
            "jobs.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    match_score = Column(
        Float,
        nullable=False
    )

    analysis = Column(
        JSON,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="job_matches"
    )

    job = relationship(
        "Job",
        back_populates="matchings"
    )