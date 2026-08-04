from sqlalchemy.orm import Session

from app.models.job_matching import JobMatching


class JobMatchingRepository:

    @staticmethod
    def create(
        db: Session,
        matching: JobMatching
    ):

        db.add(matching)

        db.commit()

        db.refresh(matching)

        return matching

    @staticmethod
    def get_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(JobMatching)
            .filter(
                JobMatching.resume_id == resume_id
            )
            .all()
        )

    @staticmethod
    def get_by_job(
        db: Session,
        job_id: int
    ):

        return (
            db.query(JobMatching)
            .filter(
                JobMatching.job_id == job_id
            )
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        matching: JobMatching
    ):

        db.delete(matching)

        db.commit()