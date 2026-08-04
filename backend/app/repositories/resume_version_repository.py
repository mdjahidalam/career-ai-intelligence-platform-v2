from sqlalchemy.orm import Session

from app.models.resume_version import ResumeVersion


class ResumeVersionRepository:

    @staticmethod
    def create(
        db: Session,
        version: ResumeVersion
    ):

        db.add(version)

        db.commit()

        db.refresh(version)

        return version

    @staticmethod
    def get_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(ResumeVersion)
            .filter(
                ResumeVersion.resume_id == resume_id
            )
            .order_by(
                ResumeVersion.version_number.desc()
            )
            .all()
        )

    @staticmethod
    def get_latest(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(ResumeVersion)
            .filter(
                ResumeVersion.resume_id == resume_id
            )
            .order_by(
                ResumeVersion.version_number.desc()
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        version: ResumeVersion
    ):

        db.delete(version)

        db.commit()