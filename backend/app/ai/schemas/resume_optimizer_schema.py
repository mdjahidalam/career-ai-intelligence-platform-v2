from typing import List, Optional

from pydantic import BaseModel, Field

from app.ai.schemas.common import (

    Skills,

    Project

)


class ResumeOptimizer(BaseModel):

    professional_summary: Optional[str] = None

    optimized_projects: List[Project] = Field(
        default_factory=list
    )

    optimized_skills: Skills

    ats_friendly_recommendations: List[str] = Field(
        default_factory=list
    )