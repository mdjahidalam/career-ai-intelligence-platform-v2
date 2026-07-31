from app.models.resume_ai_analysis import ResumeAIAnalysis

from app.repositories.resume_ai_analysis_repository import (
    ResumeAIAnalysisRepository
)

from app.core.config import settings


class ResumeAIAnalysisService:

    MODEL_NAME = "gemini-2.5-flash"

    MODEL_VERSION = "v1"

    @staticmethod
    def save_analysis(
        db,
        resume,
        parsed_json
    ):

        analysis = ResumeAIAnalysis(

            resume_id=resume.id,

            parsed_json=parsed_json,

            model_name=ResumeAIAnalysisService.MODEL_NAME,

            model_version=ResumeAIAnalysisService.MODEL_VERSION

        )

        return ResumeAIAnalysisRepository.create(
            db,
            analysis
        )