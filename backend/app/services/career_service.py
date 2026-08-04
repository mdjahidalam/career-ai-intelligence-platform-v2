from app.models.career_path import CareerPath

from app.repositories.career_path_repository import (
    CareerPathRepository
)


class CareerService:

    @staticmethod
    def save(
        db,
        resume,
        career_result
    ):

        careers = []

        recommendations = career_result.get(
            "career_recommendations",
            []
        )

        for item in recommendations:

            career = CareerPath(

                resume_id=resume.id,

                career_title=item.get(
                    "career_title"
                ),

                match_score=item.get(
                    "match_score",
                    0
                ),

                roadmap=item.get(
                    "roadmap",
                    []
                ),

                required_skills=item.get(
                    "required_skills",
                    []
                ),

                estimated_salary=item.get(
                    "estimated_salary"
                )

            )

            CareerPathRepository.create(
                db,
                career
            )

            careers.append(
                career
            )

        return careers

    @staticmethod
    def get_by_resume(
        db,
        resume_id
    ):

        return CareerPathRepository.get_by_resume(
            db,
            resume_id
        )