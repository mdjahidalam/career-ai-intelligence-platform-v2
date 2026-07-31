from typing import List, Optional

from pydantic import BaseModel, Field

from app.ai.schemas.common import (
    Skills,
    Education,
    Project,
    Experience
)


class ResumeBuilder(BaseModel):

    professional_summary: Optional[str] = None

    skills: Skills

    education: List[Education] = Field(
        default_factory=list
    )

    experience: List[Experience] = Field(
        default_factory=list
    )

    projects: List[Project] = Field(
        default_factory=list
    )

    certifications: List[str] = Field(
        default_factory=list
    )

    ats_score: int = Field(
        default=0,
        ge=0,
        le=100
    )

    recommendations: List[str] = Field(
        default_factory=list
    )