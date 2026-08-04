from app.models.skill import Skill

from app.repositories.skill_repository import (
    SkillRepository
)


class SkillService:

    @staticmethod
    def save(
        db,
        resume,
        skills
    ):

        saved = []

        for skill_name in skills:

            skill = Skill(

                resume_id=resume.id,

                skill_name=skill_name

            )

            SkillRepository.create(
                db,
                skill
            )

            saved.append(skill)

        return saved

    # ----------------------------------------

    @staticmethod
    def get_resume_skills(
        db,
        resume_id
    ):

        return SkillRepository.get_by_resume(
            db,
            resume_id
        )