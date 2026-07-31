from app.ai.orchestrator import AIOrchestrator


class LLMExtractor:

    @staticmethod
    def extract_resume(
        resume_text: str
    ):

        return AIOrchestrator.analyze_resume(
            resume_text
        )