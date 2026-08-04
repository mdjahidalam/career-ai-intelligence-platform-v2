from app.models.interview_session import (
    InterviewSession
)

from app.repositories.interview_repository import (
    InterviewRepository
)


class InterviewService:

    @staticmethod
    def save(
        db,
        resume,
        result
    ):

        interview = InterviewSession(

            resume_id=resume.id,

            session_name=result.get(
                "session_name",
                "Interview"
            ),

            company_name=result.get(
                "company_name"
            ),

            job_role=result.get(
                "job_role"
            ),

            interview_level=result.get(
                "level",
                "Beginner"
            ),

            score=result.get(
                "score",
                0
            ),

            feedback=result

        )

        return InterviewRepository.create(
            db,
            interview
        )

    # ----------------------------------------

    @staticmethod
    def get_history(
        db,
        resume_id
    ):

        return InterviewRepository.get_by_resume(
            db,
            resume_id
        )