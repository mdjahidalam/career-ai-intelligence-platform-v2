from typing import List

from pydantic import BaseModel, Field

from app.ai.schemas.common import (

    PersonalInformation,

    CareerProfile,

    Education,

    Skills,

    Project,

    Experience

)


class ResumeSchema(BaseModel):

    personal_information: PersonalInformation

    career_profile: CareerProfile

    education: List[Education] = Field(default_factory=list)

    skills: Skills

    projects: List[Project] = Field(default_factory=list)

    experience: List[Experience] = Field(default_factory=list)

    certifications: List[str] = Field(default_factory=list)

    languages: List[str] = Field(default_factory=list)