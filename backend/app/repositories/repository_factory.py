from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_ai_analysis_repository import ResumeAIAnalysisRepository
from app.repositories.job_repository import JobRepository


class RepositoryFactory:

    @staticmethod
    def resume():

        return ResumeRepository()

    @staticmethod
    def resume_analysis():

        return ResumeAIAnalysisRepository()

    @staticmethod
    def job():

        return JobRepository()