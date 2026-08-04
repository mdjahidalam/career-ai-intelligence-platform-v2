from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class Skill(Base):

    __tablename__ = "skills"

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

    skill_name = Column(
        String(150),
        nullable=False
    )

    category = Column(
        String(100)
    )

    proficiency = Column(
        Float,
        default=0.0
    )

    resume = relationship(
        "Resume",
        back_populates="skills"
    )