from sqlalchemy.orm import Session

from app.models.resume_ai_analysis import ResumeAIAnalysis



class ResumeAIAnalysisRepository:

    @staticmethod
    def create(
        db: Session,
        analysis: ResumeAIAnalysis
    ):

        db.add(analysis)

        db.commit()

        db.refresh(analysis)

        return analysis