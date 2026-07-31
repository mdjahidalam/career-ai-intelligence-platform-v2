from typing import List, Optional

from pydantic import BaseModel, Field


# ==========================================================
# Personal Information
# ==========================================================

class PersonalInformation(BaseModel):

    name: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    location: Optional[str] = None

    linkedin: Optional[str] = None

    github: Optional[str] = None


# ==========================================================
# Career Profile
# ==========================================================

class CareerProfile(BaseModel):

    career_domain: Optional[str] = None

    primary_role: Optional[str] = None

    secondary_roles: List[str] = Field(default_factory=list)

    experience_level: Optional[str] = None

    education_level: Optional[str] = None


# ==========================================================
# Education
# ==========================================================

class Education(BaseModel):

    degree: Optional[str] = None

    branch: Optional[str] = None

    college: Optional[str] = None

    cgpa: Optional[str] = None

    year: Optional[str] = None


# ==========================================================
# Skills
# ==========================================================

class Skills(BaseModel):

    programming: List[str] = Field(default_factory=list)

    frameworks: List[str] = Field(default_factory=list)

    database: List[str] = Field(default_factory=list)

    cloud: List[str] = Field(default_factory=list)

    ai_ml: List[str] = Field(default_factory=list)

    tools: List[str] = Field(default_factory=list)

    other_skills: List[str] = Field(default_factory=list)


# ==========================================================
# Project
# ==========================================================

class Project(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    technologies: List[str] = Field(default_factory=list)

    impact: Optional[str] = None


# ==========================================================
# Experience
# ==========================================================

class Experience(BaseModel):

    company: Optional[str] = None

    role: Optional[str] = None

    duration: Optional[str] = None

    description: Optional[str] = None