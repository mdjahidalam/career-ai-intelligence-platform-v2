"""
==================================================
Resume Builder Schema
Career AI Intelligence Platform
==================================================
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


# ==================================================
# Candidate Information
# ==================================================

class Candidate(BaseModel):

    name: str = Field(
        description="Candidate full name"
    )

    role: str = Field(
        description="Current or target professional role"
    )

    email: Optional[str] = Field(
        default="",
        description="Professional email address"
    )

    phone: Optional[str] = Field(
        default="",
        description="Phone number"
    )

    location: Optional[str] = Field(
        default="",
        description="Current location"
    )

    linkedin: Optional[str] = Field(
        default="",
        description="LinkedIn profile URL"
    )

    github: Optional[str] = Field(
        default="",
        description="GitHub profile URL"
    )

    portfolio: Optional[str] = Field(
        default="",
        description="Portfolio website URL"
    )

    other_links: List[str] = Field(
        default_factory=list,
        description="Additional professional links"
    )


# ==================================================
# Experience
# ==================================================

class Experience(BaseModel):

    company: str

    role: str

    duration: Optional[str] = ""

    location: Optional[str] = ""

    highlights: List[str] = Field(
        default_factory=list,
        description="3-5 ATS friendly bullet points"
    )


# ==================================================
# Project
# ==================================================

class Project(BaseModel):

    title: str

    highlights: List[str] = Field(
        default_factory=list,
        description="3-5 ATS friendly bullet points"
    )

    technologies: List[str] = Field(
        default_factory=list
    )

    impact: Optional[str] = ""


# ==================================================
# Education
# ==================================================

class Education(BaseModel):

    degree: str

    specialization: Optional[str] = ""

    institute: str

    cgpa: Optional[str] = ""

    year: Optional[str] = ""


# ==================================================
# Certification
# ==================================================

class Certification(BaseModel):

    name: str

    issuer: Optional[str] = ""

    year: Optional[str] = ""


# ==================================================
# Achievement
# ==================================================

class Achievement(BaseModel):

    title: str

    description: Optional[str] = ""


# ==================================================
# Resume Builder Output
# ==================================================

class ResumeBuilder(BaseModel):

    candidate: Candidate

    professional_summary: str

    skills: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Dynamic profession-wise skill categories"
    )

    experience: List[Experience] = Field(
        default_factory=list
    )

    projects: List[Project] = Field(
        default_factory=list
    )

    education: List[Education] = Field(
        default_factory=list
    )

    certifications: List[Certification] = Field(
        default_factory=list
    )

    achievements: List[Achievement] = Field(
        default_factory=list
    )

    languages: List[str] = Field(
        default_factory=list
    )

    ats_score: int = Field(
        ge=0,
        le=100
    )

    recommendations: List[str] = Field(
        default_factory=list
    )

