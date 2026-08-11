"""
==================================================
Microsoft Resume Template
Career AI Intelligence Platform
==================================================
"""

from docx import Document

from .helpers import ResumeHelper
from .sections import ResumeSections


class MicrosoftResumeTemplate:

    @staticmethod
    def build(
        resume_data: dict
    ):

        document = Document()

        ResumeHelper.set_document_properties(
        document
        )

        # ==========================================
        # Page Setup
        # ==========================================

        ResumeHelper.apply_page_margin(
            document
        )

        # ==========================================
        # Header
        # ==========================================

        ResumeSections.header(

            document=document,

            candidate=resume_data.get(
                "candidate",
                {}
            )

        )

        # ==========================================
        # Professional Summary
        # ==========================================

        ResumeSections.summary(

            document,

            resume_data.get(
                "professional_summary",
                ""
            )

        )

        # ==========================================
        # Skills
        # ==========================================

        ResumeSections.skills(

            document,

            resume_data.get(
                "skills",
                {}
            )

        )

        # ==========================================
        # Experience
        # ==========================================

        ResumeSections.experience(

            document,

            resume_data.get(
                "experience",
                []
            )

        )

        # ==========================================
        # Projects
        # ==========================================

        ResumeSections.projects(

            document,

            resume_data.get(
                "projects",
                []
            )

        )

        # ==========================================
        # Education
        # ==========================================

        ResumeSections.education(

            document,

            resume_data.get(
                "education",
                []
            )

        )

        # ==========================================
        # Certifications
        # ==========================================

        ResumeSections.certifications(

            document,

            resume_data.get(
                "certifications",
                []
            )

        )

        # ==========================================
        # Achievements
        # ==========================================

        ResumeSections.achievements(

            document,

            resume_data.get(
                "achievements",
                []
            )

        )

        # ==========================================
        # Languages
        # ==========================================

        ResumeSections.languages(

            document,

            resume_data.get(
                "languages",
                []
            )

        )

        return document