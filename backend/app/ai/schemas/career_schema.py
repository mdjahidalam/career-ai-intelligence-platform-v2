from typing import List

from pydantic import BaseModel, Field


class CareerRecommendation(BaseModel):

    best_roles: List[str] = Field(default_factory=list)

    alternative_roles: List[str] = Field(default_factory=list)

    best_industries: List[str] = Field(default_factory=list)

    recommended_companies: List[str] = Field(default_factory=list)


class SkillGapAnalysis(BaseModel):

    missing_skills: List[str] = Field(default_factory=list)

    recommended_courses: List[str] = Field(default_factory=list)

    priority_learning: List[str] = Field(default_factory=list)


class LearningRoadmap(BaseModel):

    next_30_days: List[str] = Field(default_factory=list)

    next_90_days: List[str] = Field(default_factory=list)

    next_180_days: List[str] = Field(default_factory=list) 