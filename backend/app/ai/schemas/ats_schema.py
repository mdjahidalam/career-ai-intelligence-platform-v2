from typing import List, Optional

from pydantic import BaseModel, Field


class ATSAnalysis(BaseModel):

    ats_score: int = Field(default=0,ge=0,le=100)

    resume_quality: Optional[str] = None

    strengths: List[str] = Field(default_factory=list)

    weaknesses: List[str] = Field(default_factory=list)

    missing_keywords: List[str] = Field(default_factory=list)

    formatting_issues: List[str] = Field(default_factory=list)

    improvement_suggestions: List[str] = Field(default_factory=list)