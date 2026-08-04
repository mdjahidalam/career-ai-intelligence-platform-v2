from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
    String,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class ResumeVersion(Base):

    __tablename__ = "resume_versions"

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

    version_number = Column(
        Integer,
        nullable=False
    )

    version_name = Column(
        String(100),
        nullable=False
    )

    resume_json = Column(
        JSON,
        nullable=False
    )

    created_by = Column(
        String(50),
        default="AI"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="versions"
    )