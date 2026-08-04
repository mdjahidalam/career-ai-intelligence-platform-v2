from sqlalchemy.orm import Session

from app.models.interview_session import InterviewSession


class InterviewRepository:

    @staticmethod
    def create(
        db: Session,
        interview: InterviewSession
    ):

        db.add(interview)
        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def get_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(InterviewSession)
            .filter(
                InterviewSession.resume_id == resume_id
            )
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        interview: InterviewSession
    ):

        db.delete(interview)
        db.commit()