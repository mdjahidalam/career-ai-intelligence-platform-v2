from sqlalchemy.orm import Session

from app.models.career_path import CareerPath


class CareerPathRepository:

    @staticmethod
    def create(
        db: Session,
        career: CareerPath
    ):

        db.add(career)

        db.commit()

        db.refresh(career)

        return career

    @staticmethod
    def get_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(CareerPath)
            .filter(
                CareerPath.resume_id == resume_id
            )
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        career: CareerPath
    ):

        db.delete(career)

        db.commit()