from typing import List

from pydantic import BaseModel, Field


class InterviewPreparation(BaseModel):

    overall_readiness: int = Field(
        default=0,
        ge=0,
        le=100
    )

    technical_questions: List[str] = Field(
        default_factory=list
    )

    hr_questions: List[str] = Field(
        default_factory=list
    )

    system_design_questions: List[str] = Field(
        default_factory=list
    )

    improvement_tips: List[str] = Field(
        default_factory=list
    )