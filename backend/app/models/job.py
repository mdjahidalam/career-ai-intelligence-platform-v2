from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_name = Column(
        String(200),
        nullable=False
    )

    job_title = Column(
        String(200),
        nullable=False
    )

    location = Column(
        String(200)
    )

    employment_type = Column(
        String(50)
    )

    experience_required = Column(
        String(100)
    )

    salary_range = Column(
        String(100)
    )

    skills_required = Column(
        Text
    )

    job_description = Column(
        Text,
        nullable=False
    )

    source = Column(
        String(100),
        default="Manual"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    matchings = relationship(
        "JobMatching",
        back_populates="job",
        cascade="all, delete-orphan"
    )