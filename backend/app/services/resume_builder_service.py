from app.ai.orchestrator.ai_orchestrator import AIOrchestrator
from app.services.resume_ai_analysis_service import ResumeAIAnalysisService


class ResumeBuilderService:

    @staticmethod
    def optimize_resume(db, resume_id: int):

        analysis = ResumeAIAnalysisService.get_by_resume(
            db,
            resume_id
        )

        if not analysis:
            return None

        return AIOrchestrator.optimize_resume(
            analysis.parsed_json
        )

    @staticmethod
    def build_resume(db, resume_id: int):

        analysis = ResumeAIAnalysisService.get_by_resume(
            db,
            resume_id
        )

        if not analysis:
            return None

        return AIOrchestrator.build_resume(
            analysis.parsed_json
        )