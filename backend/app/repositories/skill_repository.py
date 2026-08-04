from sqlalchemy.orm import Session

from app.models.skill import Skill


class SkillRepository:

    @staticmethod
    def create(
        db: Session,
        skill: Skill
    ):

        db.add(skill)
        db.commit()
        db.refresh(skill)

        return skill

    @staticmethod
    def get_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(Skill)
            .filter(
                Skill.resume_id == resume_id
            )
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        skill: Skill
    ):

        db.delete(skill)
        db.commit()