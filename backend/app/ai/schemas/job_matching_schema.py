from typing import List, Optional

from pydantic import BaseModel, Field


class JobMatching(BaseModel):

    match_score: int = Field(
        default=0,
        ge=0,
        le=100
    )

    matched_skills: List[str] = Field(
        default_factory=list
    )

    missing_skills: List[str] = Field(
        default_factory=list
    )

    missing_keywords: List[str] = Field(
        default_factory=list
    )

    strengths: List[str] = Field(
        default_factory=list
    )

    weaknesses: List[str] = Field(
        default_factory=list
    )

    recommendation: Optional[str] = None