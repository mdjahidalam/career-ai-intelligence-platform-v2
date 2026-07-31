from pydantic import BaseModel

from app.ai.schemas.resume_schema import ResumeSchema

from app.ai.schemas.ats_schema import ATSAnalysis

from app.ai.schemas.placement_schema import PlacementPrediction

from app.ai.schemas.salary_schema import SalaryPrediction

from app.ai.schemas.career_schema import (
    CareerRecommendation,
    SkillGapAnalysis,
    LearningRoadmap
)

from app.ai.schemas.interview_schema import (
    InterviewPreparation
)

from app.ai.schemas.resume_optimizer_schema import (
    ResumeOptimizer
)

from app.ai.schemas.resume_builder_schema import (
    ResumeBuilder
)

from app.ai.schemas.job_matching_schema import (
    JobMatching
)


class FinalResumeSchema(ResumeSchema):

    ats_analysis: ATSAnalysis

    placement_prediction: PlacementPrediction

    salary_prediction: SalaryPrediction

    career_recommendation: CareerRecommendation

    skill_gap_analysis: SkillGapAnalysis

    learning_roadmap: LearningRoadmap

    interview_preparation: InterviewPreparation

    resume_optimizer: ResumeOptimizer

    resume_builder: ResumeBuilder

    job_matching: JobMatching