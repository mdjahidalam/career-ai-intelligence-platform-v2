from app.models.job_matching import JobMatching
from app.repositories.job_matching_repository import (
    JobMatchingRepository
)


class JobMatchingService:

    @staticmethod
    def save(
        db,
        resume,
        job,
        result
    ):

        match = JobMatching(

            resume_id=resume.id,

            job_id=job.id,

            match_score=result.get(
                "match_score",
                0
            ),

            analysis=result

        )

        return JobMatchingRepository.create(
            db,
            match
        )

    # ----------------------------------------

    @staticmethod
    def get_resume_matches(
        db,
        resume_id
    ):

        return JobMatchingRepository.get_by_resume(
            db,
            resume_id
        )

    # ----------------------------------------

    @staticmethod
    def get_job_matches(
        db,
        job_id
    ):

        return JobMatchingRepository.get_by_job(
            db,
            job_id
        )