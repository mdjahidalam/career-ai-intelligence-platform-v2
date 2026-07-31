from pydantic import BaseModel
from typing import List, Optional


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
    secondary_roles: List[str] = []
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
    programming: List[str] = []
    frameworks: List[str] = []
    database: List[str] = []
    cloud: List[str] = []
    ai_ml: List[str] = []
    tools: List[str] = []
    other_skills: List[str] = []


# ==========================================================
# Project
# ==========================================================

class Project(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = []
    impact: Optional[str] = None


# ==========================================================
# Experience
# ==========================================================

class Experience(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[str] = None


# ==========================================================
# Technical Analysis
# ==========================================================

class TechnicalAnalysis(BaseModel):
    programming_score: int = 0
    frontend_score: int = 0
    backend_score: int = 0
    database_score: int = 0
    cloud_score: int = 0
    ai_ml_score: int = 0
    cyber_security_score: int = 0
    devops_score: int = 0
    overall_technical_score: int = 0


# ==========================================================
# Soft Skills
# ==========================================================

class SoftSkills(BaseModel):
    communication_score: int = 0
    leadership_score: int = 0
    teamwork_score: int = 0
    problem_solving_score: int = 0
    adaptability_score: int = 0
    overall_soft_skill_score: int = 0


# ==========================================================
# ATS Analysis
# ==========================================================

class ATSAnalysis(BaseModel):
    ats_score: int = 0
    resume_quality: Optional[str] = None
    strengths: List[str] = []
    weaknesses: List[str] = []
    missing_keywords: List[str] = []
    improvement_suggestions: List[str] = []


# ==========================================================
# Placement Prediction
# ==========================================================

class PlacementPrediction(BaseModel):
    placement_probability: int = 0
    confidence_score: int = 0
    hiring_recommendation: Optional[str] = None
    reasoning: List[str] = []


# ==========================================================
# Salary Prediction
# ==========================================================

class SalaryPrediction(BaseModel):
    india_salary_range: Optional[str] = None
    global_salary_range: Optional[str] = None
    reasoning: List[str] = []


# ==========================================================
# Career Recommendation
# ==========================================================

class CareerRecommendation(BaseModel):
    best_roles: List[str] = []
    alternative_roles: List[str] = []
    best_industries: List[str] = []
    recommended_companies: List[str] = []


# ==========================================================
# Skill Gap
# ==========================================================

class SkillGapAnalysis(BaseModel):
    missing_skills: List[str] = []
    recommended_courses: List[str] = []
    priority_learning: List[str] = []


# ==========================================================
# Learning Roadmap
# ==========================================================

class LearningRoadmap(BaseModel):
    next_30_days: List[str] = []
    next_90_days: List[str] = []
    next_180_days: List[str] = []


# ==========================================================
# Interview Preparation
# ==========================================================

class InterviewPreparation(BaseModel):
    overall_readiness: int = 0
    technical_questions: List[str] = []
    hr_questions: List[str] = []
    system_design_questions: List[str] = []
    improvement_tips: List[str] = []


# ==========================================================
# Resume Optimizer
# ==========================================================

class ResumeOptimizer(BaseModel):
    professional_summary: Optional[str] = None
    optimized_projects: List[Project] = []
    optimized_skills: Skills
    ats_friendly_recommendations: List[str] = []


# ==========================================================
# Job Matching
# ==========================================================

class JobMatching(BaseModel):
    match_score: Optional[int] = None
    matched_skills: List[str] = []
    missing_skills: List[str] = []
    recommendation: Optional[str] = None


# ==========================================================
# Resume Summary
# ==========================================================

class ResumeSummary(BaseModel):
    summary: Optional[str] = None


# ==========================================================
# Final Schema
# ==========================================================

class ResumeSchema(BaseModel):

    personal_information: PersonalInformation

    career_profile: CareerProfile

    education: List[Education]

    skills: Skills

    projects: List[Project]

    experience: List[Experience]

    certifications: List[str]

    languages: List[str]

    technical_analysis: TechnicalAnalysis

    soft_skills: SoftSkills

    ats_analysis: ATSAnalysis

    placement_prediction: PlacementPrediction

    salary_prediction: SalaryPrediction

    career_recommendation: CareerRecommendation

    skill_gap_analysis: SkillGapAnalysis

    learning_roadmap: LearningRoadmap

    interview_preparation: InterviewPreparation

    resume_optimizer: ResumeOptimizer

    job_matching: JobMatching

    resume_summary: ResumeSummary