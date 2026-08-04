from app.models.resume_version import ResumeVersion
from app.repositories.resume_version_repository import (
    ResumeVersionRepository
)


class ResumeVersionService:

    @staticmethod
    def create_version(
        db,
        resume,
        resume_json,
        version_name="AI Generated"
    ):

        latest = ResumeVersionRepository.get_latest(
            db,
            resume.id
        )

        if latest:

            version_number = latest.version_number + 1

        else:

            version_number = 1

        version = ResumeVersion(

            resume_id=resume.id,

            version_number=version_number,

            version_name=version_name,

            resume_json=resume_json

        )

        return ResumeVersionRepository.create(
            db,
            version
        )

    # ----------------------------------------

    @staticmethod
    def get_versions(
        db,
        resume_id
    ):

        return ResumeVersionRepository.get_by_resume(
            db,
            resume_id
        )

    # ----------------------------------------

    @staticmethod
    def latest(
        db,
        resume_id
    ):

        return ResumeVersionRepository.get_latest(
            db,
            resume_id
        )