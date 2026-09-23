from sqlalchemy.orm import Session

from app.models.user import User
from app.models.resume import Resume


class UserContextService:

    # ==========================================
    # Build AI Context For Logged-in User
    # ==========================================

    @staticmethod
    def build_context(
        db: Session,
        user: User
    ) -> dict:

        # --------------------------------------
        # Basic User Information
        # --------------------------------------

        context = {
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email
            }
        }

        # --------------------------------------
        # Get Latest Resume
        # --------------------------------------

        resume = (
            db.query(Resume)
            .filter(
                Resume.user_id == user.id
            )
            .order_by(
                Resume.uploaded_at.desc()
            )
            .first()
        )

        if resume is None:

            context["resume"] = None

            return context

        # --------------------------------------
        # Resume Information
        # --------------------------------------

        resume_context = {
            "id": resume.id,
            "filename": resume.original_filename
        }

        # --------------------------------------
        # Resume AI Analysis
        # --------------------------------------

        if resume.analysis:

            resume_context["analysis"] = (
                resume.analysis.parsed_json
            )

        else:

            resume_context["analysis"] = None

        # --------------------------------------
        # Resume Skills
        # --------------------------------------

        resume_context["skills"] = [

            {
                "name": skill.skill_name,
                "category": skill.category,
                "proficiency": skill.proficiency
            }

            for skill in resume.skills

        ]

        context["resume"] = resume_context

        return context